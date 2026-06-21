"""Generated from Smithy shape ``com.amazonaws.securityhub#ConnectionDirection``."""

from typing import Literal, TypeAlias, cast

ConnectionDirection: TypeAlias = Literal[
    "INBOUND",
    "OUTBOUND",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionDirection) -> str:
    return value


def deserialize_json(data: str) -> ConnectionDirection:
    return cast(ConnectionDirection, data)
