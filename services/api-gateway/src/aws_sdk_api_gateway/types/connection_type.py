"""Generated from Smithy shape ``com.amazonaws.apigateway#ConnectionType``."""

from typing import Literal, TypeAlias, cast

ConnectionType: TypeAlias = Literal[
    "INTERNET",
    "VPC_LINK",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionType) -> str:
    return value


def deserialize_json(data: str) -> ConnectionType:
    return cast(ConnectionType, data)
