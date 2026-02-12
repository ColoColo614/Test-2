"""Tiny web app that serves random deep thoughts on request."""

from __future__ import annotations

import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from deep_thoughts import get_random_thought

INDEX_HTML = """<!doctype html>
<html lang=\"en\">
  <head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
    <title>Deep Thought Dispenser</title>
    <style>
      body {
        margin: 0;
        min-height: 100vh;
        display: grid;
        place-items: center;
        background: linear-gradient(135deg, #edf6ff, #f7f2ff);
        font-family: Arial, sans-serif;
      }
      .card {
        width: min(680px, 92vw);
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 10px 28px rgba(20, 20, 45, 0.15);
      }
      h1 {
        margin-top: 0;
        font-size: 1.7rem;
      }
      button {
        border: 0;
        border-radius: 10px;
        background: #5b3cc4;
        color: white;
        padding: 0.75rem 1rem;
        font-size: 1rem;
        cursor: pointer;
      }
      button:hover { background: #472fa0; }
      #thought {
        margin-top: 1rem;
        line-height: 1.5;
        font-size: 1.1rem;
      }
    </style>
  </head>
  <body>
    <main class=\"card\">
      <h1>Deep Thought Dispenser</h1>
      <p>Tap the button whenever you need an odd little monologue.</p>
      <button id=\"request-btn\">Request a Deep Thought</button>
      <p id=\"thought\" aria-live=\"polite\">Your first thought is waiting...</p>
    </main>
    <script>
      async function fetchThought() {
        const response = await fetch('/api/deep-thought');
        const data = await response.json();
        document.getElementById('thought').textContent = data.thought;
      }
      document.getElementById('request-btn').addEventListener('click', fetchThought);
      fetchThought();
    </script>
  </body>
</html>
"""


class DeepThoughtHandler(BaseHTTPRequestHandler):
    def _send_json(self, payload: dict[str, str], status: HTTPStatus = HTTPStatus.OK) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_html(self, html: str, status: HTTPStatus = HTTPStatus.OK) -> None:
        body = html.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        if self.path in {"/", "/index.html"}:
            self._send_html(INDEX_HTML)
            return

        if self.path == "/api/deep-thought":
            self._send_json({"thought": get_random_thought()})
            return

        self._send_json({"error": "Not found"}, status=HTTPStatus.NOT_FOUND)


def run_server(host: str = "0.0.0.0", port: int = 8000) -> None:
    server = ThreadingHTTPServer((host, port), DeepThoughtHandler)
    print(f"Serving Deep Thought Dispenser on http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run_server()
