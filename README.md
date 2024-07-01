# CAPC-host

CAPC Host server for docker environment.

## Installation & Run

```sh
sudo pip install git+https://github.com/CA-Giken/capc-host --break-system-packages
sudo capc-host
```

# Client usage

```py
from capc_host import client

client.request_shutdown()
```

## References

- [https://qiita.com/tamo_breaker/items/dbd8482e88c61269d531]
