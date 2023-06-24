def compress_rle(data):
    compressed_data = ""
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed_data += str(count) + data[i - 1]
            count = 1
    compressed_data += str(count) + data[-1]
    return compressed_data


def decompress_rle(compressed_data):
    decompressed_data = ""
    i = 0
    if len(compressed_data) % 2 ==  0 :
        while i < len(compressed_data):
            count = int(compressed_data[i])
            char = compressed_data[i + 1]
            decompressed_data += char * count
            i += 2
        return decompressed_data
    else:
        while i < len(compressed_data)-1:
            count = int(compressed_data[i])
            char = compressed_data[i + 1]
            decompressed_data += char * count
            i += 2
        count = int(compressed_data[i])
        char = ' '
        decompressed_data += char * count
        return decompressed_data
    