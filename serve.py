#!/usr/bin/env python3
"""no-cache static server for qiji-ascend (每次改动普通刷新即可见)"""
import http.server, socketserver, sys, os

PORT = 5699
ROOT = os.path.dirname(os.path.abspath(__file__))

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    def translate_path(self, path):
        # 全部请求映射到本目录
        return super().translate_path(path)

socketserver.ThreadingTCPServer.allow_reuse_address = True
os.chdir(ROOT)
with socketserver.ThreadingTCPServer(('0.0.0.0', PORT), NoCacheHandler) as httpd:
    print(f'serving {ROOT} on :{PORT} (no-cache)', flush=True)
    httpd.serve_forever()
