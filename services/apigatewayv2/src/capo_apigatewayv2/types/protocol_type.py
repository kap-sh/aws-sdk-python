"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ProtocolType``."""

from typing import Literal, TypeAlias, cast

"""Represents a protocol type."""
ProtocolType: TypeAlias = Literal[
    "WEBSOCKET",
    "HTTP",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProtocolType) -> str:
    return value


def deserialize_json(data: str) -> ProtocolType:
    return cast(ProtocolType, data)
