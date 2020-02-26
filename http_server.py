#!/usr/bin/env python

import http.server
import socketserver

class Handler(http.server.BaseHTTPRequestHandler):
    def notfound(self):
        if '__local_aars__' in self.path:
            print('Bad request: %s' % self.path)
        self.send_response(404)
        self.end_headers()
        if self.command != 'HEAD':
            self.wfile.write(b'Not found')

    def log_message(self, format, *args):
        # Override to silence default logs
        return

    def do_GET(self):
        self.notfound()

    def do_HEAD(self):
        self.notfound()

with socketserver.TCPServer(("", 5000), Handler) as httpd:
    httpd.serve_forever()
