import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading


def execute(cmd: str):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)

    return output.decode()


class NetKitty:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()

    def send(self):
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)

        try:
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096:
                        break
                    if response:
                        print(response)
                        buffer = input('> ')
                        buffer += '\n'
                        self.socket.send(buffer.encode())
        except KeyboardInterrupt:
            print('User terminated.')
            self.socket.close()
            sys.exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='NetKitty - The Ultimate Tool for All Things Furrious...',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
        das_netkitty.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt # upload a file
        das_netkitty.py -t 192.168.1.108 -p 5555 -l -c # command shell
        das_netkitty.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # execute command
        das_netkitty.py -t 192.168.1.108 -p 5555 # connect to server
        echo 'FOO' | ./netcat.py -t 192.168.1.108 -p 135 # echo text to server port 135
        '''))

    parser.add_argument('-c', '--command', action='store_true', help='command shell')
    parser.add_argument('-e', '--execute', help='execute specified command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
    parser.add_argument('-t', '--target', default='192.168.1.11', help='specified address')
    parser.add_argument('-u', '--upload', help='upload file')
    args = parser.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()

    nk = NetKitty(args, buffer.encode())
    nk.run()
