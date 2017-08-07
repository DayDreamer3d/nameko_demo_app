from nameko import rpc


# initial records to start with
records = {
    'Smith': {'age': 23, 'active': True},
    'Andy': {'age': 41, 'active': True},
    'John': {'age': 12, 'active': True},
}


class DbService(object):
    """ Mock database class to imitate an ORM.
        or database transactional service. 
    """
    name = 'db_service'

    @rpc.rpc
    def get_records(active=True):
        """ Get the records from the mock database records.
        """
        return [
            (name, info['age'])
            for name, info in records.items()
            if active
        ]

