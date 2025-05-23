import time

import pika, sys

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='recon_task', durable=True)

    def callback(ch, method, properties, body):
        b = body.split(b'|')
        tts = int.from_bytes(b[1]) - 48
        print(f" [x] Received {str(b[0])}")
        print(tts)
        for i in range(tts):
            print(f"  [-] counting {tts - i}")
            time.sleep(1)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='hello', on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
