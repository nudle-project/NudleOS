import os
os.access("mips.cpp")
def mipsArcitecture64():
    #impl mips64
    print("mips64 test ", int(1))
    for mips in range(10):
        print("MIPS 64-bit test number:", int(2))
    pass
def mipsArcitecture32():    #impl mips32
    print("mips32 test ", int(1))
    for mips in range(10):
        print("MIPS 32-bit test number:", int(3))
    pass
class MipsISA():
    def __init__(self, bits):
        self.bits = bits
    def run(self):
        if self.bits == 64:
            mipsArcitecture64()
        elif self.bits == 32:
            mipsArcitecture32()
        else:
            print("Unsupported MIPS architecture")
            pass
    mov = 0x00af0
    add = 0x00af1
    sub = 0x00af2
    mul = 0x00af3
    div = 0x00af4
    mod = 0x00af5
    and_ = 0x00af6
    or_ = 0x00af7
    xor = 0x00af8
    not_ = 0x00af9
    shl = 0x00afa
    shr = 0x00afb
    jmp = 0x00afc
    je = 0x00afd
    jne = 0x00afe
    jg = 0x00aff
    jge = 0x00b00
    jl = 0x00b01
    jle = 0x00b02
    call = 0x00b03
    ret = 0x00b04
    push = 0x00b05
    pop = 0x00b06
    nop = 0x00b07
    hlt = 0x00b08
    #end