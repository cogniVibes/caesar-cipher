# Caesar Cipher

Caesar Cipher is one of the oldest and simplest encryption algorithms. It is named after Julius Caesar, who used it to communicate secretly with his generals. The idea behind Caesar Cipher is to replace each letter in the plaintext with a letter that is a fixed number of positions down the alphabet. For example, if the key is 3, then each letter in the plaintext will be replaced by the letter that is three positions down the alphabet. Thus, 'A' becomes 'D', 'B' becomes 'E', 'C' becomes 'F', and so on.

## How it works

Caesar Cipher works by shifting each letter in the plaintext by a fixed number of positions down the alphabet. The number of positions shifted is known as the key or the shift value. The formula for encrypting a letter using Caesar Cipher is:

`E(x) = (x + k) mod 26`

where `x` is the numerical value of the letter (A=0, B=1, C=2, ..., Z=25), `k` is the key or the shift value, and `mod 26` means to take the remainder when divided by 26.

To decrypt a letter, the formula is:

`D(x) = (x - k) mod 26`

where `x` is the numerical value of the encrypted letter, `k` is the key or the shift value, and `mod 26` means to take the remainder when divided by 26.

## Example

Suppose the plaintext is "HELLO" and the key is 3. Then each letter in the plaintext is shifted by 3 positions down the alphabet, according to the encryption formula:

```
H -> K
E -> H
L -> O 
L -> O
O -> R
```

So the ciphertext is "KHOOR". To decrypt the ciphertext, we simply shift each letter back by 3 positions, according to the decryption formula:

```
K -> H
H -> E
O -> L
O -> L
R -> O
```

So the plaintext is "HELLO" again.

## Encryption table

To make it easier to perform encryption and decryption, we can create a table that shows the correspondence between the plaintext letters and the ciphertext letters, as well as the numerical values of the letters. Suppose the key is 3 then the encrption table will look like this.

| Letter | A | B | C | D | E | F | *--snip--* | U | V | W | X | Y | Z |
|--------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Encrypted Letter** | D | E | F | G | H | I | *--snip--* | X | Y | Z | A | B | C |

