import os
import zlib

def encode_block(block):
    return bytes(byte ^ 0xAB for byte in block)

def encode_file(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        exe_data = f_in.read()

    compressed_data = zlib.compress(exe_data)

    block_size = 512
    encoded_data = bytearray()

    for i in range(0, len(compressed_data), block_size):
        block = compressed_data[i:i + block_size]
        encoded_data.extend(encode_block(block))

    with open(output_file, 'wb') as f_out:
        f_out.write(encoded_data)

    print(f"Đã mã hóa file EXE và lưu vào {output_file}")


if __name__ == "__main__":
    input_exe = 'test7v1.exe'  
    output_txt = 'encoded_file.bin'  

    encode_file(input_exe, output_txt)
