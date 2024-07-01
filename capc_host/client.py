import socket
from typing import Union

TIMEOUT = 60
BUFFER = 1024
HOSTNAME = "localhost"
PORT = 33010


class SocketClient:
    def __init__(self, timeout: int = TIMEOUT, buffer: int = BUFFER) -> None:
        self._socket: Union[socket.socket, None] = None
        self._address: Union[tuple[str, int], None] = None
        self._timeout = timeout
        self._buffer = buffer

    def connect(self) -> None:
        self._address = (HOSTNAME, PORT)
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self._socket.settimeout(self._timeout)
        if self._address is None:
            print("Address is not set.")
            return
        self._socket.connect(self._address)

    def send(self, message: str = "") -> None:
        if self._socket is None:
            print("Socket is not set.")
            return

        flag = False
        while True:
            if message == "":
                message = input("> ")
            else:
                message_send = message
                flag = True
            self._socket.send(message_send.encode("utf-8"))
            message_recv = self._socket.recv(self._buffer).decode("utf-8")
            self.received(message_recv)
            if flag:
                break

        try:
            self._socket.shutdown(socket.SHUT_RDWR)
            self._socket.close()
        except Exception as e:
            print(e)
            pass

    def received(self, message: str) -> None:
        print("[Client] Received -> ", message)


if __name__ == "__main__":
    client = SocketClient()
    client.connect()
    client.send("Test message.")
