"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ProtocolType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_apigatewayv2.errors import DeserializationError
from aws_sdk_apigatewayv2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""Represents a protocol type."""
ProtocolType: TypeAlias = Literal[
    "WEBSOCKET",
    "HTTP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WEBSOCKET",
        "HTTP",
    )
)


def serialize_json(value: ProtocolType) -> str:
    return value


def deserialize_json(data: str) -> ProtocolType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProtocolType value: {data!r}")
    return cast(ProtocolType, data)
