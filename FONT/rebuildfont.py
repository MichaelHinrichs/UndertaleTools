import os
import struct
import codecs
def get_font_chars(name):
    fp = open(name , "rb")
    lines = fp.readlines()
    alist = []
    for line in lines:
        if "," in line:
            v0 = line.split(',')[:5]
            char_id , x, y, w, h = int(v0[0]),int(v0[1]),int(v0[2]),int(v0[3]),int(v0[4])
            alist.append((char_id , x, y, w, h))
    fp.close()
    return alist

def buildfont(csv_name , dest_name):
    alist = get_font_chars(csv_name)
    chs_font_width = 18
    en_font_width = 8
    dest = open(dest_name , 'wb')
    dest.write(struct.pack("I",0))
    dest.write(struct.pack("I",0))
    dest.write(struct.pack("I",12))
    dest.write(struct.pack("I",1))
    dest.write(struct.pack("I",0))
    dest.write(struct.pack("H",alist[0][0]))
    dest.write(struct.pack("H",1))
    dest.write(struct.pack("H",alist[-1][0]))
    dest.write(struct.pack("H",0))
    dest.write(struct.pack("I",0x100b1a))
    dest.write('\x00\x00\x80\x3f')
    dest.write('\x00\x00\x80\x3f')
    dest.write(struct.pack("I",len(alist)))
    dest.write('\x00\x00\x00\x00' * len(alist))
    for i in xrange(len(alist)):
        (char_id , x, y, w, h) = alist[i]
        dest.write(struct.pack("H",char_id))
        dest.write(struct.pack("H",x))
        dest.write(struct.pack("H",y))
        dest.write(struct.pack("H",w))
        dest.write(struct.pack("H",h))
        if char_id <= 0x7e:
            dest.write(struct.pack("H",en_font_width))
        else:
            dest.write(struct.pack("H",chs_font_width))
        dest.write(struct.pack("H",1))
        dest.write(struct.pack("H",0))
    dest.close()
buildfont("font.csv" , "font.bin")






