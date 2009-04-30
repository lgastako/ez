import logging
import wsgiref.handlers
from webob import Request

import config

logger = logging.getLogger(__name__)


def main():
    controller_map = config.controller_map()
    config.routes.create_regs(controller_map.keys())
    def handler(environ, start_response):
        request = Request(environ)
        logger.debug("Trying to match request path: %s" % request.path)
        request.route_info = config.routes.match(request.path)
        logger.debug("route info: %s" % str(request.route_info))
        controller_name = request.route_info["controller"]
        controller = controller_map.get(controller_name)
        if not controller:
            raise Exception("Could not find controller for name: %s" % controller_name)
        action = getattr(controller, request.route_info["action"])
        response = action(request)
        # response = controller.action(request)
        return response(environ, start_response)
    wsgiref.handlers.CGIHandler().run(handler)


if __name__ == '__main__':
    main()
