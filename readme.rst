Demo App
========


Introduction
------------

In this setup we will use Nameko to create an app with following functionalities.
- setup for http traffic and http service.
- rpc for inter-service calls.
- event based logging.

.. note::
    It's a demo app therefore, we are using Nameko for both http and rpc traffic.
    We are mocking database as well as logging bits too.
    In real world we would prefer appropriate technologies for each of these parts.


Setup
-----

We will create three services
- ``http_route_service`` - service facing client, accepts and responds to http requests.
- ``db_service`` - interact with low level persistent infrastructure.
- ``log_service`` - event based logging service and write logs to file.

Make sure RabbitMQ is running and ``localhost:8000`` is free.
Use ``nameko run db_service log_service route_service`` to start these services.


Working
-------

.. image:: demo-app.png
	:alt: demo app image
#. Client will send a ``GET`` http request through ``localhost:8000``.
#. ``http_route_service`` will receive this request and sends an rpc request to RabbitMQ.
#. Broker will route this message to ``database_service`` to get the records from persistent store.
#. These records will get returned to ``http_route_service`` which will use them to fill the ``html template``.
#. ``http_route_service`` will also dispatch ``get_people`` event for logging to RabbitMQ broker.
#. Event message will get routed to ``log_service`` which writes this message to a file.
#. Finally, ``http_route_service`` returns the http response with html.

|
