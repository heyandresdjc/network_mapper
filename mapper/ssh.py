from sshtunnel import SSHTunnelForwarder, BaseSSHTunnelForwarderError, HandlerSSHTunnelForwarderError
from main import map_network

for ip in map_network():
    print("Checking... ", ip)
    try:
        server = SSHTunnelForwarder(
            ip,
            ssh_username="pi",
            remote_bind_address=('127.0.0.1', 8080)
        )
        server.start()
        print(server.local_bind_port)  # show assigned local port
        # work with `SECRET SERVICE` through `server.local_bind_port`.
        server.stop()
    except BaseSSHTunnelForwarderError:
        print("Couldn't connect to...", ip)
    except HandlerSSHTunnelForwarderError:
        print("Failed... ", ip)
    except Exception as ex:
        print(ex.__str__())
