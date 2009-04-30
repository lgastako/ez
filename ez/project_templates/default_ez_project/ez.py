import os
import inspect

from mako.lookup import TemplateLookup
from webob import Response

_template_lookup = None

def get_template_lookup():
    global _template_lookup
    if not _template_lookup:
        _template_lookup = TemplateLookup(directories=[os.path.join(os.path.dirname(__file__), 'templates')])
    return _template_lookup


def render(vars=None, template_path=None, template_type=".html"):
    if not template_path:
        stack = inspect.stack()
        action_name = stack[1][3]
        controller_file = stack[1][1]
        controller_name = controller_file.split("/")[-1].split(".")[0]
        template_path = os.path.join("x", controller_name, action_name + template_type)[1:]
    response = Response()
    response.body = get_template_lookup().get_template(template_path).render(stack=stack, **vars)
    return response
