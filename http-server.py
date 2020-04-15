from http.server import HTTPServer, SimpleHTTPRequestHandler

class EchoRequestHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        content = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(content)
    def do_GET(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(b'It works!')

httpd = HTTPServer(('localhost', 7654), EchoRequestHandler)
print ('Http server started on http://{}:{}'.format(httpd.server_name, httpd.server_port))
httpd.serve_forever()
