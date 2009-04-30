# This function needs to return a dictionary mapping controller names to
# controller namespaces (modules or classes).  The simple, idiomatic way to
# do this is to just import each controller (optionally with one or more
# aliases) directly into this function and then return locals(), like so:
#
# def controller_map():
#     from controllers import users
#     from controllers import images
#     from some.thirdparty.package import AuthController as auth
#     return locals()

def controller_map():
    from controllers import home
    return locals()


# TODO: Document routes
from routes import Mapper

routes = Mapper()
routes.connect(':controller/:action/:id')
routes.connect('', controller='home')
