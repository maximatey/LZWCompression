def LZWcompress(data):
    dictionary = {chr(i): i for i in range(128)}
    next_code = 128
    compressed_data = []
    current_sequence = ""

    for char in data:
        current_sequence += char
        if current_sequence not in dictionary:
            compressed_data.append(bin(dictionary[current_sequence[:-1]])[2:].zfill(8))
            dictionary[current_sequence] = next_code
            next_code += 1
            current_sequence = char

    if current_sequence in dictionary:
        compressed_data.append(bin(dictionary[current_sequence])[2:].zfill(8))

    compressed_data = ' '.join(compressed_data)

    return compressed_data

def LZWdecompress(compressed_data):
    compressed_data = compressed_data.split()
    dictionary = {i: chr(i) for i in range(128)}
    next_code = 128
    decompressed_data = []
    current_code = int(compressed_data.pop(0), 2)
    decompressed_data.append(dictionary[current_code])

    for code in compressed_data:
        if int(code, 2) in dictionary:
            entry = dictionary[int(code, 2)]
        elif int(code, 2) == next_code:
            entry = dictionary[current_code] + dictionary[current_code][0]
        else:
            raise ValueError("Invalid compressed data")

        decompressed_data.append(entry)

        dictionary[next_code] = dictionary[current_code] + entry[0]
        next_code += 1
        current_code = int(code, 2)

    return ''.join(decompressed_data)
