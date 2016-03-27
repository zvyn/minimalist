#!/usr/bin/python3
from http.server import HTTPServer as H, BaseHTTPRequestHandler as B
H(('', 8000), type('', (B, ), {'do_GET': lambda s: s.wfile.write(
    b'HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=UTF-8\r\n\r\n'
    b'Hello World\r\n')})).serve_forever()
