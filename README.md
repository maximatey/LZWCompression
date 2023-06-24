# LZWCompression

This repository contains the source code fot a webapp that is used for compressing and decompressing strings using LZW algorithm and RLE algorithm.

# Requirements
* Python 3.11
* Django 4.2.2

   Visit the `requirements.txt` file for more requirements

# How to launch
Deployed App:
* Visit https://lzw-compression.vercel.app

Local:
* Download this repository
* Open the terminal for the repository
* Run `py manager.py runserver`

# Application Algorithms
## Compression
For both LZW and RLE, the input is a string, formed by the 255 valid ASCII characters
* LZW

  The LZW algorithm shall output a string containing bytes, which length is determined by the input

  The function used shall take the input, for each character, the function will check if the current character and the following character has been recorded, if not, it will add it in a local dictionary with an id (which starts from 128, increasing for each addition to the dictionary) and the current character's id/ASCII code will be recorded for the output. This id will be used for next time if the current character and the following character appears in the string to be recorded for the output. This significantly reduces the amount of bytes used to store a string that is long and contains reconcurring string of characters.
  
* RLE

  The RLE algorithm shall output a string that has been encoded through the RLE algorithm

  RLE is a simple compression algorithm that reduces the size of data by replacing consecutive repeated characters with a count and a single instance of that character. It works by scanning through the data and grouping adjacent identical characters together. Instead of storing each repeated character individually, RLE stores the count of the repetitions followed by the character itself.

## Decompression
* LZW

  The LZW algoritm decompresses itself from its bytes form into a string of characters by backtracking the compression process.

* RLE

  The RLE reconstruct itself easily by repeating the character by the amount of character times, which is contained in the string the algorithm compresses into.

# Sub-repositories
* Front-end : https://github.com/maximatey/LZWCompression-FE
  
* Back-end : https://github.com/maximatey/LZWCompression-BE
# Author
Alex Sander (https://github.com/maximatey)

  
