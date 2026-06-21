"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CryptoWalletNetwork``."""

from typing import Literal, TypeAlias, cast

"""<p>Supported blockchain networks for crypto wallets.</p>"""
CryptoWalletNetwork: TypeAlias = Literal[
    "ETHEREUM",
    "SOLANA",
]


# --- restJson1 ser/de ---
def serialize_json(value: CryptoWalletNetwork) -> str:
    return value


def deserialize_json(data: str) -> CryptoWalletNetwork:
    return cast(CryptoWalletNetwork, data)
