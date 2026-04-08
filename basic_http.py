import socket
import json
from dice import Dice

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server socket to an IP address and port
PORT = 8081
server_socket.bind(('localhost', PORT))

# Start listening for incoming connections
server_socket.listen(1)
print(f"Server is listening on port {PORT}...")

# Accept incoming client connections
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} established.")
    
    # Receive the HTTP request from the client
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Request received ({len(request)}):")
    print("*"*50)
    print(request)
    print("*"*50)

    # Check if the request is a GET request
    if request.startswith("GET /roll_dice"):
        print("Someone called roll_dice!")
        print("Split: ")
        print(request.splitlines())
        print("===========")
        my_dice = None
        try:
            # VERY unsafe, but whatever lol
            data_dict = eval(request.splitlines()[-1])
            print("THIS data!: ",data_dict)
            my_dice = Dice(data_dict['probabilities'],data_dict['number_of_random'])
            my_dice.roll_dice()
        except Exception as e:
            print(f"Error decoding data...: {e}")
        status = "error"
        
        response_data = {
            "status": status,
            "message": "Hello, KU!",
        } # JSON response example
        
        if my_dice != None:
            status = "success"
            response_data["dice"] = my_dice.results
        

        # Convert dictionary to JSON string
        response_json = json.dumps(response_data)

        # HTTP response with JSON content
        response = f"""HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{response_json}"""
    elif request.startswith("GET"):
        # Prepare an HTTP response (basic HTML)
        response = f"""HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
                        <html><body><h1>Hello, World!</h1><hr>{request}</body></html>"""
    else:
        # Respond with a 405 Method Not Allowed if not a GET request
        response = "HTTP/1.1 405 Method Not Allowed\r\n\r\n"

    client_socket.sendall(response.encode('utf-8')) # Send the HTTP response to the client

    client_socket.close() # Close the client connection
    
    print("Waiting for the next TCP request...")
