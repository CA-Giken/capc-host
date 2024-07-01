#!/usr/bin/env python3

# 特定ポートへのソケット通信を監視するモジュール
import socket
from typing import Union

from capc_host.responder import respond_action

TIMEOUT = None
BUFFER = 1024
HOSTNAME = "localhost"
PORT = 33010


class SocketServer:
    def __init__(self, hostname: str = HOSTNAME, port: int = PORT, buffer: int = BUFFER) -> None:
        self._socket: Union[socket.socket, None] = None
        self._timeout = None
        self._buffer = buffer
        self.address = (hostname, port)
        self.reconnectionCount = 0
        self.close()

    def __del__(self) -> None:
        self.close()

    def close(self) -> None:
        if self._socket is None:
            return
        try:
            self._socket.shutdown(socket.SHUT_RDWR)
            self._socket.close()
        except Exception:
            pass

    def accept(self) -> None:
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self._socket.settimeout(self._timeout)
        self._socket.bind(self.address)
        self._socket.listen(1)
        print("Server started :", self.address)
        conn, _ = self._socket.accept()
        while True:
            try:
                message_recv = conn.recv(self._buffer).decode("utf-8")
                message_resp = self.respond(message_recv)
                conn.send(message_resp.encode("utf-8"))
            except ConnectionResetError:
                # 接続張り直し
                self.accept()
                break
            except BrokenPipeError:
                # 接続張り直し
                self.accept()
                break

    def respond(self, message: str) -> str:
        print("[Server] Received -> ", message)
        message_resp = respond_action(message)

        return message_resp


def main() -> None:
    server = SocketServer()
    server.accept()


if __name__ == "__main__":
    main()
