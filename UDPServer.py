import socket

def main() -> None:
    """
    Main function to create and bind a UDP socket,
    receive messages, and send a response back to the client.

    Args:
        None

    Returns:
        None
    """
    # Create a UDP socket
    sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Bind the socket to a specific IP address and port
        server_address: tuple = ('localhost', 12345)
        sock.bind(server_address)
    except OSError:
        print("Socket is already open!")
        return

    # Set to store client addresses
    clients: set = set()

    while True:
        # Wait for a message to be received
        print('Waiting for a message...')
        data, address = sock.recvfrom(4096)
        print(f'Received message: {data.decode()}')

        # Add the client address to the set
        clients.add(address)

        # Broadcast the message to all connected clients
        for client_address in clients:
            if client_address != address:
                message: str = f'{address}: {data.decode()}'
                sock.sendto(message.encode(), client_address)

if __name__ == '__main__':
    main()
