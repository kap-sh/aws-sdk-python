"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BlockchainChainId``."""

from typing import Literal, TypeAlias, cast

"""<p>Supported blockchain chain identifiers for balance queries. Each value maps to a specific chain supported by the underlying providers (Privy, Coinbase).</p>"""
BlockchainChainId: TypeAlias = Literal[
    "BASE",
    "BASE_SEPOLIA",
    "ETHEREUM",
    "SOLANA",
    "SOLANA_DEVNET",
]


# --- restJson1 ser/de ---
def serialize_json(value: BlockchainChainId) -> str:
    return value


def deserialize_json(data: str) -> BlockchainChainId:
    return cast(BlockchainChainId, data)
