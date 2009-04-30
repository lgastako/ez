from paste.script.templates import Template
from paste.script.templates import var


class EzProjectTemplate(Template):
    _template_dir = "project_templates/default_ez_project"
    summary = "An ez web framework project"
    vars = [
        var("gae_app_name", "Google AppEngine app name (all lowercase, no spaces)", default="my_app"),
    ]
