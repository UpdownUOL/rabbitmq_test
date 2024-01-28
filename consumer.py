#!/usr/bin/python

from oslo_config import cfg
import oslo_messaging

rabbitmq_admin ="admin"
rabbitmq_password ="admin123"

transport_url = 'rabbit://%s:%s@127.0.0.1:5672/' %(rabbitmq_admin,rabbitmq_password)
transport = oslo_messaging.get_transport(cfg.CONF, transport_url)
target = oslo_messaging.Target(topic='test')
client = oslo_messaging.RPCClient(transport, target)
r = client.call({}, 'test', a=2, b=3)
print(r)
print("success")