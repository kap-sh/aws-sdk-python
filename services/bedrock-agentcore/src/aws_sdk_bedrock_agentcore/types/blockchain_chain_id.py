"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BlockchainChainId``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

"""<p>Supported blockchain chain identifiers for balance queries. Each value maps to a specific chain supported by the underlying providers (Privy, Coinbase).</p>"""
BlockchainChainId: TypeAlias = Literal[
    "BASE",
    "BASE_SEPOLIA",
    "ETHEREUM",
    "SOLANA",
    "SOLANA_DEVNET",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASE",
        "BASE_SEPOLIA",
        "ETHEREUM",
        "SOLANA",
        "SOLANA_DEVNET",
    )
)


def serialize_json(value: BlockchainChainId) -> str:
    return value


def deserialize_json(data: str) -> BlockchainChainId:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlockchainChainId value: {data!r}")
    return cast(BlockchainChainId, data)
