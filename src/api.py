"""
This is a simple HTTP server, serving at localhost:9000
It takes an URL from the file 'bannero.txt' (Randomly gets a line)
And the makes a 301 redirect to the image url
"""

import random
import http.server as webserver
import socketserver

PORT = 9000

class banneroHandler(webserver.SimpleHTTPRequestHandler):
  def do_GET(self):
    # Read file: bannero.txt
    f = open('./src/bannero.txt', 'r')
    # Get random line, then strip out ending newline '\n'
    url = getRandomUrl(f).strip()
    print(url)

    # Redirect url
    self.send_response(301)
    self.send_header('Location', url)
    self.end_headers()

# Get random line from image file
# Code from StackOverflow: https://bit.ly/2U2NsrP
def getRandomUrl(file):
  lines = next(file)
  for num, line in enumerate(file, 2):
    if random.randrange(num):
      continue
    lines = line
  return lines

def main():
  # Start HTTP server
  handler = socketserver.TCPServer(("", PORT), banneroHandler)
  print('Serving at port', PORT)
  handler.serve_forever()

if __name__ == "__main__":
    main()