import os
import websockets
import handler

PORT = int(os.environ.get("PORT", 9999))
start_server = websockets.serve(handler, "0.0.0.0", PORT)
