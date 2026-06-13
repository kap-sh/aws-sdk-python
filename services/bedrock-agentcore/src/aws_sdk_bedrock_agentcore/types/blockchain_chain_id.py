"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BlockchainChainId``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore.errors import DeserializationError
from aws_sdk_bedrock_agentcore._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>Supported blockchain chain identifiers for balance queries. Each value maps to a specific chain supported by the underlying providers (Privy, Coinbase).</p>"""
BlockchainChainId: TypeAlias = Literal["BASE", "BASE_SEPOLIA", "ETHEREUM", "SOLANA", "SOLANA_DEVNET",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BASE", "BASE_SEPOLIA", "ETHEREUM", "SOLANA", "SOLANA_DEVNET",))


def serialize_json(value: BlockchainChainId) -> str:
    return value


def deserialize_json(data: str) -> BlockchainChainId:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlockchainChainId value: {data!r}")
    return cast(BlockchainChainId, data)