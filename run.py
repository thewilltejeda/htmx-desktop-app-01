import webview
from threading import Thread, Event
from app import app  # Assuming app.py is your Flask application

# This event will be set when we need to stop the Flask server
stop_event = Event()

app_title = "Stock Prices App"
host = "http://127.0.0.1"
port = 5000

def run():
    while not stop_event.is_set():
        app.run(port=port, use_reloader=False)

if __name__ == '__main__':
    t = Thread(target=run)
    t.daemon = True  # This ensures the thread will exit when the main program exits
    t.start()

    webview.create_window(
        app_title,
        f"{host}:{port}",
        resizable=False,
        height=710,
        width=225,
        frameless=True,
        easy_drag=True,
        on_top=True
        )
    
    webview.start()

    stop_event.set()  # Signal the Flask server to shut down
