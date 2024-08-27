
from client import Client
from itertools import product
from server import Server
import argparse
import csv
import ipaddress
import json
import os
import pandas as pd
import socket
import sys
import threading
import time

SERVER_DATA = "data.csv"
CLIENT_DATA = "client_data.csv"
SERVER_ROWS = ["NAME", "STATUS", "IP_ADDRESS",
               "UDP_PORT", "TCP_PORT", "FILENAMES"]
CLIENT_ROWS = ["FILENAME", "OWNER", "CLIENT IP ADDRESS", "PORT"]
PROMPT = "$ >>> "


def main() -> None:
    """Begin either the server or client."""

    client = Client()
    server = Server()


if __name__ == "__main__":
    """Run main."""
    main()
