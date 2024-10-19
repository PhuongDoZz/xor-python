import zlib

def decode_block(block):
    return bytes(byte ^ 0xAB for byte in block)

def decode_file(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        encoded_data = f_in.read()

    block_size = 512
    compressed_data = bytearray()

    for i in range(0, len(encoded_data), block_size):
        block = encoded_data[i:i + block_size]
        compressed_data.extend(decode_block(block))

    original_data = zlib.decompress(compressed_data)

    with open(output_file, 'wb') as f_out:
        f_out.write(original_data)

    print(f"Đã giải mã file và lưu vào {output_file}")

if __name__ == "__main__":
    input_txt = 'encoded_file.bin'  
    output_exe = 'decoded_file.exe'  

    decode_file(input_txt, output_exe)
