import socket
from response import Response
from health import parse_data


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    PORT = 7979
    s.bind(("127.0.0.1", PORT))
    s.listen()
    print(f"listening on port {PORT}")

    while True:
        conn, addr = s.accept()
        with conn:
            data = conn.recv(8192)
            if not data:
                conn.close()
                continue

            response = Response(parse_data(), headers={
                "Access-Control-Allow-Origin": "*"
            })

            print("\nRESPONSE\n", str(response))
            conn.sendall(bytes(str(response), "UTF-8"))