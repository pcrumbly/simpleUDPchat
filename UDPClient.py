import socket

def is_socket_open(sock: socket.socket) -> bool:
    """
    Check if a socket is open by attempting to bind to it.
    Returns True if the bind operation succeeds, False otherwise.
    """
    try:
        sock.bind(('localhost', 0))
        return True
    except OSError:
        return False

def main() -> None:
    """
    Main function to create and bind a UDP socket,
    send and receive messages to/from the server.
    """
    # Create a UDP socket
    sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address: tuple = ('localhost', 12345)

    if not is_socket_open(sock):
        print("Socket is already open!")
        return

    try:
        while True:
            # Get user input
            message: str = input("Enter a message to send: ")

            # Send the message to the server
            sock.sendto(message.encode(), server_address)

            # Receive response from the server
            data: bytes
            address: tuple
            data, address = sock.recvfrom(4096)
            print(f'Received response: {data.decode()}')
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        sock.close()

if __name__ == '__main__':
    main()
