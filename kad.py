import asyncio
import argparse
import logging
from threading import Thread
from kademlia.network import Server
from IPython import embed

DEFAULT_PORT = 5678

class KadNode:

    @staticmethod
    def set_logging():
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        log = logging.getLogger('kademlia')
        log.addHandler(handler)
        log.setLevel(logging.DEBUG)

    def __init__(self, port=DEFAULT_PORT,  evt_loop=None):
        self.set_logging()
        if not evt_loop:
            evt_loop = asyncio.get_event_loop()
        self.loop = evt_loop
        self.node = Server()
        self.port = port
        self.start_server()

    def start_server(self):
        def start_loop(node,  port):
            server_loop = asyncio.new_event_loop()
            server_loop.run_until_complete(
                node.listen(port)
            )
            try:
                server_loop.run_forever()
            except KeyboardInterrupt:
                pass
            finally:
                node.stop()
                server_loop.close()
        #
        t = Thread(target=start_loop, args=(self.node, self.port))
        t.start()

    def boot_to(self, host, port):
        self.loop.run_until_complete(
            self.node.bootstrap([(host, port), ])
        )

    def set(self, key, value):
        self.loop.run_until_complete(
            self.node.set(key, value)
        )

    def get(self, key):
        result = self.loop.run_until_complete(
            self.node.get(key)
        )
        return result


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", required=True, help="UDP port to listen ON", type=int)
args = parser.parse_args()

if __name__ == '__main__':
    # start Kademlia server node
    k = KadNode(port=args.port)
    # embed ipython shell
    embed(using=False)

