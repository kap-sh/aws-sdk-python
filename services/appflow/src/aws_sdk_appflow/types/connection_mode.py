"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectionMode``."""

from typing import Literal, TypeAlias, cast

ConnectionMode: TypeAlias = Literal[
    "Public",
    "Private",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionMode) -> str:
    return value


def deserialize_json(data: str) -> ConnectionMode:
    return cast(ConnectionMode, data)
