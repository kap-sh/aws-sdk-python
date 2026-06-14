"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ProtocolType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apigatewayv2.errors import DeserializationError

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
