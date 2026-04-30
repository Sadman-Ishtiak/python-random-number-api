from http.server import BaseHTTPRequestHandler
import random
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        number = random.randint(1, 100)
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
        response = {
            "random_number": number
        }
        
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return
