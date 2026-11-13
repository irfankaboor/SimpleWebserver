
from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
    pass

server_address = ('127.0.0.1', 8000)

httpd = HTTPServer(server_address, MyHandler)

print("Server started successfully!")
print("Open http://127.0.0.1:8000")

httpd.serve_forever()
