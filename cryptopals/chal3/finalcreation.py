
from chal2 import bytes_xor
frequencies = {'a': 0.07566239439048221,
 'b': 0.013701936892924881,
 'c': 0.026047473992758204,
 'd': 0.048083223173745616,
 'e': 0.13156790620150582,
 'f': 0.024464049658026323,
 'g': 0.016618771193746766,
 'h': 0.05589114316914765,
 'i': 0.061509282142651875,
 'j': 0.0012385769297086039,
 'k': 0.004968676360710386,
 'l': 0.036214724984194493,
 'm': 0.02958503362262199,
 'n': 0.06962469107419966,
 'o': 0.07211333984711765,
 'p': 0.017113052474280133,
 'q': 0.0009282142651876545,
 'r': 0.05967584343927812,
 's': 0.05986263578366573,
 't': 0.08560262084027817,
 'u': 0.029731593769756884,
 'v': 0.010882809356859589,
 'w': 0.021185125581929996,
 'x': 0.0019426403816311282,
 'y': 0.02231450083338123,
 'z': 0.000614977872291511,
 'A': 0.0012213345594574401,
 'B': 0.000738548192424852,
 'C': 0.000614977872291511,
 'D': 0.00037645841715041093,
 'E': 0.0008937295246853268,
 'F': 0.000620725329041899,
 'G': 0.0005833668601643772,
 'H': 0.0009023507098109086,
 'I': 0.009149951146617622,
 'J': 0.00020403471463877233,
 'K': 8.908557963101328e-05,
 'L': 0.00037645841715041093,
 'M': 0.0008736134260589689,
 'N': 0.00039944824415196275,
 'O': 0.0004712914535318122,
 'P': 0.0005143973791597218,
 'Q': 2.8737283751939767e-06,
 'R': 0.00031323639289614346,
 'S': 0.0010058049313178918,
 'T': 0.0018794183573768606,
 'U': 0.0001982872578883844,
 'V': 0.00012644404850853497,
 'W': 0.0008276337720558652,
 'X': 5.7474567503879534e-06,
 'Y': 0.00046554399678142423,
 'Z': 0.0}

def score_text(text: bytes) -> float:
    # lower scores are better
    score = 0.0
    l = len(text)
    
    for letter, frequecy_expected in frequecy_expecteds.items():
        frequency_actual = text.count(ord(letter)) / l
        err = abs(frequency_expected - frequency_actual)
        score += err 
    
    return score

def crack_xor_cipher(ciphertext: bytes) -> bytes:
    best_guess = (float('inf'), None)
    
    for candidate_key in range(256):
        full_key = bytes([candidate_key]) * len(ciphertext)
        plaintext = bytes_xor(full_key, ciphertext)
        score = score_text(plaintext)
        curr_guess = (score, plaintext)
        best_guess = min(best_guess, curr_guess)
    if best_guess[1] is None:
        exit("no key found (this should never happen:)")
    return best_guess[1]


def crack_xor_cipher_worse(ciphertext: bytes) -> bytes:
    results = []
    
    for candidate_key in range(256):
        full_key = bytes([candidate_key]) * len(ciphertext)
        plaintext = bytes_xor(full_key, ciphertext)
        score = score_text(plaintext)
        curr_guess = (score, plaintext)
        results.appent(curr_guess)
    
    results.sort()
    return results[:5]

ciphertext = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
from pprint import pprint
pprint(crack_xor_cipher_worse(ciphertext))