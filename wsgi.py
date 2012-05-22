import bottle
import os

def application(environ, start_response):
    data = "Hello World! AppFog Python Support"
    start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
            ])
    return iter([data])

