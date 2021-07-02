from hashlib import sha256
import time


def apply_sha256(text):
    return sha256(text.encode('ascii')).hexdigest()

def mining_bitcoin(num_block, transations, previous_hash, zeros_qtd):
    nonce = 0

    while True:
        text = str(num_block) + transations + previous_hash + str(nonce)
        my_hash = apply_sha256(text)
        if my_hash.startswith("0" * zeros_qtd):
            return nonce, my_hash
        nonce +=1

if __name__ == "__main__":
    num_block = 15
    transations = """
    val -> peter -> 10
    peter -> bob -> 5
    bob -> camila -> 15
    """
    zeros_qtd = 5
    previous_hash = "abc" 
    start = time.time()
    result = mining_bitcoin(num_block, transations, previous_hash, zeros_qtd)
    print(result)
    print(time.time() - start)

