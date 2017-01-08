from pyramid.view import view_config
from theme_and_variations.services import make_composition as composer


@view_config(route_name='home', renderer='templates/index.pt')
def my_view(request):
    return {}


@view_config(route_name='generated', renderer='templates/generated.pt')
def composer_view(request):
    comp = composer.make_composition()
    return {'composition': comp}
