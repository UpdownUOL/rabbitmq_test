#!/usr/bin/python
from oslo_config import cfg
import oslo_messaging
import sys
import time


class TestEndpoint(object):

    def test(self, ctx, a, b):
        print("receive client access")
        return a + b


rabbitmq_admin ="admin"
rabbitmq_password ="admin123"

transport_url = 'rabbit://%s:%s@127.0.0.1:5672/' %(rabbitmq_admin,rabbitmq_password)
server = sys.argv[1]
transport = oslo_messaging.get_transport(cfg.CONF, transport_url)
target = oslo_messaging.Target(topic='test', server=server)
endpoints = [
    TestEndpoint(),
]
server = oslo_messaging.get_rpc_server(transport, target, endpoints)
try:
    server.start()
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("")
    print("Stopping server")

server.stop()
server.wait()