from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

# リクエストハンドラ
class CustomHTTPRequestHandler(BaseHTTPRequestHandler):

    # Get
    def do_GET(self):

        # レスポンスコード
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # コンテンツ
        html_context = '<html lang="ja">' \
                       '  <head>' \
                       '    <meta charset="UTF-8">' \
                       '    <title>はじめてのWebサーバー</title>' \
                       '  </head>' \
                       '  <body>' \
                       '    <p>Hello,World</p>' \
                       '  </body>' \
                       '</html>'

        self.wfile.write(html_context.encode())

# アドレス
server_address = ('localhost', 8080)

# Webサーバー起動
with HTTPServer(server_address, CustomHTTPRequestHandler) as server:
    server.serve_forever()
