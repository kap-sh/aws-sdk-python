"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ConnectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apigatewayv2.errors import DeserializationError

"""<p>Represents a connection type.</p>"""
ConnectionType: TypeAlias = Literal[
    "INTERNET",
    "VPC_LINK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERNET",
        "VPC_LINK",
    )
)


def serialize_json(value: ConnectionType) -> str:
    return value


def deserialize_json(data: str) -> ConnectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionType value: {data!r}")
    return cast(ConnectionType, data)
