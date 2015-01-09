#Created by narenarya
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid.session import UnencryptedCookieSessionFactoryConfig


from .models import (
    DBSession,
    Base,
    Paste,
    )

#using jinja2 instead of chamelion
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('pastes', '/pastes')
    config.add_route('edit', '/edit')
    config.add_route('delete', '/delete')

    config.scan()
    return config.make_wsgi_app()
