from web3 import Web3
import eth_account
from eth_account.messages import encode_defunct


def sign(m):
    w3 = Web3()

    # Create a new Ethereum account
    Account = eth_account.Account
    account_object = Account.create()
    public_key = account_object.address
    private_key = account_object.key

    # Encode the message using Ethereum's standard message prefix
    message = encode_defunct(text=m)
    signed_message = Account.sign_message(message, private_key)

    print('Account created:\n'
          f'private key={w3.to_hex(private_key)}\naccount={public_key}\n')
    
    assert isinstance(signed_message, eth_account.datastructures.SignedMessage)

    return public_key, signed_message


def verify(m, public_key, signed_message):
    w3 = Web3()

    # Encode the message in the same way it was during signing
    Account = eth_account.Account
    message = encode_defunct(text=m)

    # Recover the address from the signed message
    signer = Account.recover_message(message, signature=signed_message.signature)

    # Check if the recovered address matches the provided public key
    valid_signature = (signer.lower() == public_key.lower())

    assert isinstance(valid_signature, bool), "verify should return a boolean value"
    return valid_signature


if __name__ == "__main__":
    import random
    import string

    for i in range(10):
        m = "".join([random.choice(string.ascii_letters) for _ in range(20)])

        pub_key, signature = sign(m)

        # Modifies every other message so that the signature fails to verify
        if i % 2 == 0:
            m = m + 'a'

        if verify(m, pub_key, signature):
            print("Signed Message Verified")
        else:
            print("Signed Message Failed to Verify")
