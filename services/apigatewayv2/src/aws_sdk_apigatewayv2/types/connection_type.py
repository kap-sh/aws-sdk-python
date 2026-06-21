"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ConnectionType``."""

from typing import Literal, TypeAlias, cast

"""<p>Represents a connection type.</p>"""
ConnectionType: TypeAlias = Literal[
    "INTERNET",
    "VPC_LINK",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionType) -> str:
    return value


def deserialize_json(data: str) -> ConnectionType:
    return cast(ConnectionType, data)
