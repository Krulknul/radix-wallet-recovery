from bip_utils import Bip39SeedGenerator, Bip32Slip10Ed25519
from radix_engine_toolkit import *
import random


def initialize_account(mnemonic: str, index: int = 0):
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

    # Derivation path I found in the json backup file exported by the Babylon wallet. Pretty weird path, but it works. Last number is the account index, so this is the first one for me.
    slip10_ctx = Bip32Slip10Ed25519.FromSeedAndPath(
        seed_bytes, f"m/44'/1022'/1'/525'/1460'/{index}'"
    )

    # Get private and public keys as hex
    private_key_hex = slip10_ctx.PrivateKey().Raw().ToHex()

    # Convert to RET types
    private_key_bytes: bytes = int(private_key_hex, 16).to_bytes(32, "big")
    private_key: PrivateKey = PrivateKey.new_ed25519(private_key_bytes)
    public_key: PublicKey = private_key.public_key()

    account_address = derive_virtual_account_address_from_public_key(public_key, 1)

    return {
        "private_key": private_key,
        "public_key": public_key,
        "account_address": account_address,
    }
