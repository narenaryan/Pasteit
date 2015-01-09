from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound

from pyramid.view import view_config
import time

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    Paste,
    )


@view_config(route_name='edit')
def edit(request):
    if request.POST:
        user = DBSession.query(Paste)
        print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
        print user
    return {}
    
@view_config(route_name='delete')
def delete(request):
    if request.POST:
        print request.POST.get('user')
        one = DBSession.query(Paste).filter_by(email=request.POST.get('user')).first()
        print one.text
    return {}

# /howdy?name=alice which links to the next view
@view_config(route_name='pastes',renderer='templates/pastes.jinja2')
def pastes(request):
    foo = DBSession.query(Paste).all()
    return {'pastes':foo,'edit_url': request.route_url('edit'),'delete_url': request.route_url('delete')}


@view_config(route_name='home', renderer='templates/index.jinja2',request_method=['GET','POST'])
def home(request):
    if  request.POST:
        email = request.params.get('email')
        text = request.params.get('text')
        paste = Paste(email=email, text=text,time=time.ctime())
        DBSession.add(paste)
        return HTTPFound(location = request.route_url('pastes'))
    return {'url':request.route_url('home')}

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_listing_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

