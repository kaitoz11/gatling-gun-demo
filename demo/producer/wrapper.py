import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='recon_task', durable=True)

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!|5', properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent))

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!|2', properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent))

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!|1', properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent))

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!|3', properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent))
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!|4', properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent))
connection.close()
