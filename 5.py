# Rail-Fence Transposition Cipher
def rail_fence_encrypt():
    word = list(input("Enter the plain text: "))
    even, odd  = [word[i] for i in range(0, len(word), 2)], [word[i] for i in range(1, len(word), 2)]
    return ''.join(even) + ''.join(odd)

def rail_fence_decrypt():
    word = list(input("Enter the plain text: "))
    if(len(word) % 2 == 0):
        odd, even = word[: int(len(word) / 2)], word[int(len(word) / 2): ]
    else:
        odd, even = word[: int(len(word) / 2) + 1], word[int(len(word) / 2) + 1:]
    if (len(odd) != len(even)):
        even.append(' ')
    plain = [odd[i] + even[i] for i in range(len(odd))]
    return ''.join(plain)
a = rail_fence_encrypt()
print(a)
b = rail_fence_decrypt()
print(b)
