# XOR Encryption - Educational Purpose

## Overview

This project demonstrates how to implement XOR encryption and decryption in Python. XOR (Exclusive OR) is a basic encryption technique used to obfuscate data by applying a bitwise XOR operation between the data and a key. This project is intended for educational purposes, illustrating both encoding and decoding of a file using XOR encryption along with basic compression using `zlib`.

![XOR Encryption Image](https://media.discordapp.net/attachments/1297198528531009536/1297198528795246613/image-213.png?ex=67150dc6&is=6713bc46&hm=cd77e7fe5d8ae030bddb999aef0d0c81ebb0d1f62d1d8bbd6ae833e2918193d9&)
100% encrypted malware image

## What is XOR?

XOR (Exclusive OR) is a logical operation that compares two bits and returns `1` if the bits are different, and `0` if they are the same. XOR encryption works by applying the XOR operation between the data and a key, making it difficult for unauthorized parties to understand the encrypted data unless they have the correct key.

### Example of XOR:

Let's take two binary numbers as an example:
- Data: `10101010`
- Key:  `11001100`

Perform XOR on each bit:

| Data | Key  | XOR Result |
|------|------|------------|
| 1    | 1    | 0          |
| 0    | 1    | 1          |
| 1    | 0    | 1          |
| 0    | 0    | 0          |
| 1    | 1    | 0          |
| 0    | 1    | 1          |
| 1    | 0    | 1          |
| 0    | 0    | 0          |

XOR Result: `01100110`

This XOR result represents the encrypted data.

## Python XOR Encryption Algorithm

The encryption method in this project applies XOR to blocks of data, with each byte in the block being XOR-ed against a fixed key (`0xAB`). The data is also compressed using the `zlib` library to minimize file size before encryption.

### Encryption Process:
1. **Read the file**: The input file (e.g., an EXE) is read in binary mode.
2. **Compress the file**: Data is compressed using `zlib`.
3. **XOR encryption**: The compressed data is encrypted using a block-based XOR method.
4. **Save the encoded file**: The encoded data is written to a binary file.

### Decryption Process:
1. **Read the encoded file**: The encrypted file is read in binary mode.
2. **XOR decryption**: The encoded data is decrypted using XOR on the same key.
3. **Decompress the data**: The decrypted data is decompressed back to its original form.
4. **Save the decoded file**: The final result is saved as a new binary file (e.g., EXE).

## Limitations

- The project does **not** include features like `--icon=icon.ico` and `--version-file=version.txt` for packaging or executable metadata. This is due to the fact that XOR encryption is not suitable for protecting application-level metadata.
- XOR encryption by itself is weak when used with a fixed key and no additional security measures, making it vulnerable to cryptanalysis if used in real-world applications.

## How to Run

1. Place your EXE file in the same directory as the script.
2. Run the `encode_file` script to encrypt the EXE.
3. Run the `decode_file` script to decrypt the encoded file back to its original form.

```bash
python main.py
python main1.py

Note:

This project is purely for educational purposes. It shows basic encryption principles and is not meant to provide any real security for sensitive data.
