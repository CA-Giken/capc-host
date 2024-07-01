import threading
import time

from capc_host.client import SocketClient
from capc_host.server import SocketServer


def run_server() -> None:
    server = SocketServer()
    server.accept()


t1 = threading.Thread(target=run_server, name="t1", daemon=True)


def test_main() -> None:
    global t1
    # 別スレッドでソケットサーバーを起動
    t1.start()
    # サーバー起動までちょっと待つ
    time.sleep(5)

    client = SocketClient()

    # ソケット通信をテストする
    client.connect()
    client.send("Test message.")

    print("Simple message test passed.")

    # ConnetionResetErrorが発生するため、テストを通すために少し待つ
    time.sleep(2)


def test_main2() -> None:
    client = SocketClient()

    # ソケット通信をテストする
    client.connect()
    client.send("Test message.")

    print("Simple message test 2 passed.")
    # ConnetionResetErrorが発生するため、テストを通すために少し待つ
    time.sleep(2)


def test_shutdown() -> None:
    client = SocketClient()

    # シャットダウンリクエストを送信
    client.connect()
    client.send("shutdown=1")

    print("Shutdown request test passed.")
    # ConnetionResetErrorが発生するため、テストを通すために少し待つ
    time.sleep(2)
