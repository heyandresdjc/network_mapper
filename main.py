from mapper.main import map_network, check_ip


print('Mapping...')
for ip in map_network():
    print(check_ip(ip, (21, 22)))
