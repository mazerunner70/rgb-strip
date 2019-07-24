from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from demo.full import FullDemo
PORT_NUMBER = 2280


# This class will handles any incoming request from
# the browser
class myHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send the html message

        if self.path == '/full-demo':
            self.run_full()
        else:
            # self.wfile.write("Hello World !" + self.path)
            self.load_file()
        return

    def run_full(self):
        self.wfile.write("Starting full demo")
        fulldemo = FullDemo()
        fulldemo.doall()

    def load_file(self):
        with open('webpage'+self.path, 'r') as myfile:
            data = myfile.read()
            self.wfile.write(data)

try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ', PORT_NUMBER

    # Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
