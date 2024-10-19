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
2. Run the `main` script to encrypt the EXE.
3. Run the `main1` script to decrypt the encoded file back to its original form.

bash
```python main.py```
```python main1.py```

Note:

This project is purely for educational purposes. It shows basic encryption principles and is not meant to provide any real security for sensitive data.



Dưới đây là file README.md bằng tiếng Việt dựa trên yêu cầu của bạn:

# Mã hóa XOR - Mục đích giáo dục

## Tổng quan

Dự án này trình bày cách triển khai mã hóa và giải mã XOR bằng Python. XOR (Exclusive OR) là một kỹ thuật mã hóa cơ bản, được sử dụng để làm rối dữ liệu bằng cách thực hiện phép toán XOR giữa dữ liệu và khóa. Dự án này nhằm mục đích giáo dục, minh họa quá trình mã hóa và giải mã một tệp bằng mã hóa XOR cùng với việc nén dữ liệu cơ bản bằng `zlib`.

![Mã hóa XOR](https://media.discordapp.net/attachments/1297198528531009536/1297198528795246613/image-213.png?ex=67150dc6&is=6713bc46&hm=cd77e7fe5d8ae030bddb999aef0d0c81ebb0d1f62d1d8bbd6ae833e2918193d9&)
Hình ảnh phần mềm độc hại được mã hóa 100%

## Mã hóa XOR là gì?

XOR (Exclusive OR) là một phép toán logic so sánh hai bit và trả về `1` nếu hai bit khác nhau, và `0` nếu chúng giống nhau. Mã hóa XOR hoạt động bằng cách thực hiện phép toán XOR giữa dữ liệu và một khóa, khiến dữ liệu mã hóa trở nên khó hiểu trừ khi bạn có khóa chính xác.

### Ví dụ về XOR:

Hãy lấy hai số nhị phân làm ví dụ:
- Dữ liệu: `10101010`
- Khóa:  `11001100`

Thực hiện XOR trên từng bit:

| Dữ liệu | Khóa | Kết quả XOR |
|--------|------|-------------|
| 1      | 1    | 0           |
| 0      | 1    | 1           |
| 1      | 0    | 1           |
| 0      | 0    | 0           |
| 1      | 1    | 0           |
| 0      | 1    | 1           |
| 1      | 0    | 1           |
| 0      | 0    | 0           |

Kết quả XOR: `01100110`

Kết quả này đại diện cho dữ liệu đã được mã hóa.

## Thuật toán mã hóa XOR trong Python

Phương pháp mã hóa trong dự án này áp dụng XOR cho các khối dữ liệu, với mỗi byte trong khối được XOR với một khóa cố định (`0xAB`). Dữ liệu cũng được nén bằng thư viện `zlib` để giảm kích thước trước khi mã hóa.

### Quá trình mã hóa:
1. **Đọc file**: Tệp đầu vào (ví dụ: tệp EXE) được đọc ở chế độ nhị phân.
2. **Nén file**: Dữ liệu được nén bằng `zlib`.
3. **Mã hóa XOR**: Dữ liệu nén được mã hóa bằng phương pháp XOR theo khối.
4. **Lưu tệp đã mã hóa**: Dữ liệu mã hóa được ghi vào tệp nhị phân.

### Quá trình giải mã:
1. **Đọc tệp mã hóa**: Tệp đã mã hóa được đọc ở chế độ nhị phân.
2. **Giải mã XOR**: Dữ liệu mã hóa được giải mã bằng XOR với cùng một khóa.
3. **Giải nén dữ liệu**: Dữ liệu giải mã được giải nén về dạng ban đầu.
4. **Lưu tệp đã giải mã**: Kết quả cuối cùng được lưu dưới dạng tệp nhị phân mới (ví dụ: EXE).

## Hạn chế

- Dự án **không** bao gồm các tính năng như `--icon=icon.ico` và `--version-file=version.txt` cho việc đóng gói hoặc metadata của tệp thực thi. Điều này là do mã hóa XOR không phù hợp để bảo vệ metadata cấp ứng dụng.
- Mã hóa XOR tự nó khá yếu khi sử dụng với một khóa cố định mà không có các biện pháp bảo mật bổ sung, làm cho nó dễ bị tấn công phân tích mật mã nếu áp dụng trong các ứng dụng thực tế.

## Cách chạy chương trình

1. Đặt tệp EXE của bạn vào cùng thư mục với mã lệnh.
2. Chạy script `main` để mã hóa tệp EXE.
3. Chạy script `main1` để giải mã tệp đã mã hóa về lại dạng ban đầu.

bash
```python main.py```
```python main2.py```

Lưu ý:

Dự án này hoàn toàn dành cho mục đích giáo dục. Nó chỉ trình bày các nguyên tắc mã hóa cơ bản và không nhằm mục đích bảo mật dữ liệu nhạy cảm.
