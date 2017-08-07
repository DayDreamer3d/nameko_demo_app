import datetime
from nameko import events


class LogService(object):
    """ Mock logging service which writes the logs
        to the text file.
    """
    # name of the service
    name = 'log_service'

    # log file name
    log_file = 'log.txt'

    @events.event_handler('http_route_service', 'get_people')
    def log(self, data):
        """ Evetn handler for "add_person" event from "http_route_service".
            Log the action and data associated with it.
        """
        # form the message
        message = '[ {} ]: ( get_people ) action with {} args has been logged.'.format(
            str(datetime.datetime.now()),
            str(data),
        )

        # log to the file
        with open(self.log_file, 'a') as f:
            f.write(message + '\n')
