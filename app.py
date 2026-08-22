from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        message = """
        <html>
        <head>
            <title>GitHub Actions Docker</title>
        </head>

        <body>
            <h1>Hello from Docker!</h1>

            <h2>GitHub Actions Docker Build</h2>

            <p>
                This application was built using
                GitHub Actions.
            </p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(message.encode())


server = HTTPServer(("0.0.0.0", 5000), Handler)

print("Server running on port 5000")

server.serve_forever()
