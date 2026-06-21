"""Generated from Smithy shape ``com.amazonaws.securityhub#NetworkDirection``."""

from typing import Literal, TypeAlias, cast

NetworkDirection: TypeAlias = Literal[
    "IN",
    "OUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkDirection) -> str:
    return value


def deserialize_json(data: str) -> NetworkDirection:
    return cast(NetworkDirection, data)
