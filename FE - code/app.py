from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer


PORT = 8000


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=".", **kwargs)


if __name__ == "__main__":
    with TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"Open http://127.0.0.1:{PORT}/Bizdi.html")
        httpd.serve_forever()
