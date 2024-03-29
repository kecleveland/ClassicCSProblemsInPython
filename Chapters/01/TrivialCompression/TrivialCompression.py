class CompressedGene:
    # constructor
    def __init__(self, gene: str) -> None: # __ not easily discoverable outside of the class
        self._compress(gene)  # _ private

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1 # sentinel
        for nucleotide in gene.upper():
            self.bit_string << 2 #shift left 2 bits
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide: {}".format(nucleotide))
    
    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2): # -1 to exclude sentinel
            bits: int = self.bit_string >> i & 0b11 # get the 2 relevant bits
            if bits == 0b00:
                gene+= "A"
            elif bits == 0b01:
                gene += "C"
            elif bits ==0b10:
                gene += "G"
            elif bits == 0b11:
                gene+= "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
            return gene[::-1] # reverse by slicing backwards
    
    def __str__(self): # str representation
        return self.decompress()

# if __name__ == "__main__":
#     from sys import getsizeof
#     original: str = "" * 100 # get original bytes using str # TODO GET ORIGINAL
#     print("original is {} bytes".format(getsizeof(original)))
#     compressed: CompressedGene = CompressedGene(original)
#     print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
#     print(compressed)
#     print("original and decompressed are the same: {}".format(original == compressed.decompress()))




