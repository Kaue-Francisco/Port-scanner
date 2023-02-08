import socket

#ip para teste de invasao
ip = 'bancocn.com'

#portas mais utilizadas - Cloudflare
ports = [20,21,22,25,53,80,123,179,443,500,3389]

#scan das portas e seu resultado
for i in ports:
   client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   client.settimeout(0.2)
   connection = client.connect_ex((ip,i))
   if connection == 0:
       print(i, '>>> OPEN')
   else:
       pass