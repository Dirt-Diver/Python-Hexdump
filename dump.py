#! usr/bin/python3

#### USAGE #### 

import sys
import argparse

def open_files(infile, outfile=None):
    try:
        if outfile:
            infile = open(str(infile), 'rb')
            outfile = open(str(outfile), 'a')
            return(infile, outfile)
        else:
            infile = open(str(infile), 'rb')
            return(infile)
    except FileNotFoundError:
        parser.print_help()
        sys.exit(0)
    except Exception as e:
        print(e)

def get_ascii_string(chunk):
    
    string = []
    for i in chunk:
        if 32<=i<=126:
            string.append(chr(i))
        else:
            string.append(".")
    string = ''.join(string)
    
    return(string)

def get_hex_string(chunk):
    
    hex_list = []
    for i in chunk:
        hex_list.append(format(i,"02x"))

    chunk = []
    for i in range(0, len(hex_list), 2):
        couplet = ''.join(hex_list[i:i+2])
        chunk.append(couplet)

    hex_list = ' '.join(chunk)

    return(hex_list)

def main():

    parser = argparse.ArgumentParser(description='Hexdump of a file')
    parser.add_argument('infile', type=str, metavar='', help='input file')
    parser.add_argument('-o', '--outfile', type=str, metavar='', help='output file')
    args = parser.parse_args()
    
    offset=0

    if args.outfile:
        infile, outfile = open_files(str(args.infile), str(args.outfile))
    else:
        infile = open_files(str(args.infile))
    
    while True:
        chunk = infile.read(16)
        if not chunk:
            break
        
        ascii_string = get_ascii_string(chunk)
        hex_string = get_hex_string(chunk)

        line = f"{offset*16:08x}: {hex_string:40} {ascii_string}"
        try :
            outfile.write(line+"\n")
            print(line)
        except:
            print(line)
        offset+=1
    try:
        outfile.close()
        infile.close()
    except:
        infile.close()


if __name__=='__main__':

    main()

