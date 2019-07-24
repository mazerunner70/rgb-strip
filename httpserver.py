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
        self.wfile.write("Hello World !"+self.path)
        if self.path == '/full':
            self.run_full()
        return

    def run_full(self):
        fulldemo = FullDemo()
        fulldemo.doall()


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
