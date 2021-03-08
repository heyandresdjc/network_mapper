import requests
from socket import *


def get_my_ip():
    """
    Find my IP address
    :return:
    """
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def map_network(pool_size=255):
    """
    Maps the network
    :param pool_size: amount of parallel ping processes
    :return: list of valid ip addresses
    """
    # get my IP and compose a base like 192.168.1.xxx
    ip_parts = get_my_ip().split('.')
    base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'
    return [base_ip + str(i) for i in range(pool_size)]


def check_ip(ip: str, ports: tuple=None):
    print("Started ")
    successful_connection = []
    if ports is None:
        ports = (80, 9000,)
    start, end = ports
    for port in range(start, end):
        try:
            conn = f"http://{ip}:{port}"
            r = requests.get(conn)
            if 200 <= r.status_code < 300:
                successful_connection.append(conn)
        except requests.RequestException:
            pass

    return successful_connection


if __name__ == '__main__':
    print('Mapping...')
    results = []
    for ip in map_network():
        print(check_ip(ip, (21, 22)))
