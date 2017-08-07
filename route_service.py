import json
from nameko import rpc, events
from nameko.web import handlers


html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Person's Age App</title>
</head>
<body>
    <h2>People's age</h2>
    <ul>
        %s
    </ul> 
</body>
</html>
"""


class RouteService(object):
    """ Class to route the http traffic
    """
    # name of the service
    name = 'http_route_service'

    # response headers
    headers = {
        'Content-Type': 'text/html'
    }

    # extensions
    db = rpc.RpcProxy('db_service')
    dispatch = events.EventDispatcher()

    @handlers.http('GET', '/')
    def index(self, request):
        """ Method for handle get method call at '/' path
        """
        # get people records from database
        people = self.db.get_records()

        # dispatch an event for logging
        self.dispatch('get_people', people)

        # line items from people
        people = [
            '<li>{}: {}</li>'.format(name, age)
            for name, age in people
        ]
        people = ' '.join(people)

        # fill the template
        content = html_template % people

        return 200, self.headers, content
