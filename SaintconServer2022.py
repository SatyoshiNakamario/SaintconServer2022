#This is an example from Saintcon 2022 for exploitability in modern software development.

import http.server
import socketserver
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    phrase = str.encode("Hello World")

    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(Handler.phrase)

if __name__ == '__main__':
    httpd = socketserver.TCPServer(('', 8000), Handler)
    httpd.serve_forever()