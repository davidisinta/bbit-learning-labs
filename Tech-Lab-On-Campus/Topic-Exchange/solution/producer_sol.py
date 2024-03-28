import argparse

import producer_interface
import pika
import os
import sys


class mqProducer(producer_interface.mqProducerInterface):

    def __init__(self,routing_key: str, exchange_name: str  ):
        self.routing_key = routing_key
        self.exchange_name = exchange_name


        self.setupRMQConnection()



    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)

        # Establish Channel
        self.channel = self.connection.channel()

        # Create the exchange if not already present
        self.exchange_name = self.channel.exchange_declare(
    exchange="Exchange Name", exchange_type="topic"
)
)



    def publishOrder(self, message: str) -> None:
        # Basic Publish to Exchange
        self.channel.basic_publish(
            exchange="Exchange Name",
            routing_key="Routing Key",
            body="Message",
        )

        # Close Channel
        self.channel.close()


        # Close Connection
        self.connection.close()















