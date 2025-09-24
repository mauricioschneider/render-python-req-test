import http.server
import socketserver

# Define the port the server will listen on
PORT = 8080

# Define a custom handler that serves "Hello, World!"
class SimpleHelloWorldHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Check if the request path is the root path
        if self.path == '/':
            # Set the response status code and headers
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            # Define the message to send
            message = "Hello, World!"
            # Write the message to the response body, encoded as bytes
            self.wfile.write(bytes(message, "utf8"))
        else:
            # For any other path, return a 404 Not Found
            self.send_error(404)

# Create the server instance
with socketserver.TCPServer(("", PORT), SimpleHelloWorldHandler) as httpd:
    print(f"Serving at port {PORT}")
    print(f"Access it at http://localhost:{PORT}/")

    # Start the server and keep it running
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()
