import socket
import time

def main():
    server_ip = "127.0.0.1"
    server_port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            # Send request for color
            client_socket.sendto("request_color".encode("utf-8"), (server_ip, server_port))

            # Receive color from server
            color, _ = client_socket.recvfrom(1024)
            color = color.decode("utf-8")

            print(f"Color received: {color}")

            # Prompt user for translation
            response = input("Enter the color in Indonesian: ")

            # Translate color and check correctness
            indonesian_color = english_to_indonesian_color(color)
            if response.lower() == indonesian_color:
                print("Correct answer! Feedback score: 100")
            else:
                print("Wrong answer. Feedback score: 0")

            # Wait before sending another request
            time.sleep(10)

    except KeyboardInterrupt:
        print("\nClient stopped.")

    finally:
        client_socket.close()
def english_to_indonesian_color(english_color):
    color_mapping = {
        "red": "merah",
        "green": "hijau",
        "blue": "biru",
        "yellow": "kuning",
        "pink": "merah-muda",
        "purple": "ungu",
        "brown": "coklat",
        "cyan":"sian",
        "maroon":"merah-marun"
    }
    return color_mapping.get(english_color.lower(), "can't find specified colors")

if __name__ == "__main__":
    main()
