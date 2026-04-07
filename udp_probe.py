import socket
import time

def udp_probe(host, port=33434, timeout=2):
    start = time.time()

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(timeout)

        sock.sendto(b"probe", (host, port))
        sock.recvfrom(1024)

        rtt = (time.time() - start) * 1000
        sock.close()

        return rtt

    except socket.timeout:
        sock.close()
        return None