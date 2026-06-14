"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CryptoWalletNetwork``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

"""<p>Supported blockchain networks for crypto wallets.</p>"""
CryptoWalletNetwork: TypeAlias = Literal[
    "ETHEREUM",
    "SOLANA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ETHEREUM",
        "SOLANA",
    )
)


def serialize_json(value: CryptoWalletNetwork) -> str:
    return value


def deserialize_json(data: str) -> CryptoWalletNetwork:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CryptoWalletNetwork value: {data!r}")
    return cast(CryptoWalletNetwork, data)
