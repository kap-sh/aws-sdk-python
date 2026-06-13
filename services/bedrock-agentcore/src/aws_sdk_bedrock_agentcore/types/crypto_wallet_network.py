"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CryptoWalletNetwork``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore.errors import DeserializationError
from aws_sdk_bedrock_agentcore._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>Supported blockchain networks for crypto wallets.</p>"""
CryptoWalletNetwork: TypeAlias = Literal["ETHEREUM", "SOLANA",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ETHEREUM", "SOLANA",))


def serialize_json(value: CryptoWalletNetwork) -> str:
    return value


def deserialize_json(data: str) -> CryptoWalletNetwork:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CryptoWalletNetwork value: {data!r}")
    return cast(CryptoWalletNetwork, data)