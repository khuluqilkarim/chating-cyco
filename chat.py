import socket
import threading
from datetime import datetime

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Koneksi terputus.")
            break

def gettime():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H:%M")
    return formatted_time

def send_message(client_socket, nama):
    while True:
        inputMessage = input()
        time = gettime()
        message = f'[{time}] {nama} : {inputMessage}'
        client_socket.send(message.encode('utf-8'))

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = "103.76.129.93"
    server_port = 31213

    try:
        client_socket.connect((server_address, server_port))
        
        nama = input("Masukkan username: ")
        client_socket.send(nama.encode('utf-8'))

        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()

        send_thread = threading.Thread(target=send_message, args=(client_socket, nama))
        send_thread.start()
    except:
        print("Tidak dapat terhubung ke server.")

if __name__ == "__main__":
    main()
