def _bytes_xor(a: bytes, b: bytes, quiet=True, check_lens=False) -> bytes:
    if not quiet:
        print(a, "xors", b)
    if check_lens and len(a) != len(b):
        raise ValueError('Length mismatch: {}!= {}'.format(len(a), len(b)))
    return bytes(byte_1 ^ byte_2 for byte_1, byte_2 in zip(a, b))

def bytes_xor(*args: bytes, quiet=True, check_lens=False):
    assert len(args) > 0 #looks for errors will kill this application 
    resutls = args[0]
    for arg in args[1:]:
        result = _bytes_xor(result, arg, quiet=quiet, check_lens=check_lens)
    return result


if __name__ == '__main__':
    a = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    b = bytes.fromhex("686974207468652062756c6c277320657965")
    result = bytes_xor(a, b, quiet=False)
    