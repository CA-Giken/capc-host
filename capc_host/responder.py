#!/usr/bin/env python3

import subprocess


def respond_action(message: str) -> str:
    if message == "shutdown=1":
        subprocess.call(["shutdown", "-h", "now"])
        return "Shutdown request is in progress."
    else:
        return "Unrecognized message."
