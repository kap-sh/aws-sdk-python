"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectionScope``."""

from typing import Literal, TypeAlias, cast

ConnectionScope: TypeAlias = Literal[
    "DOMAIN",
    "PROJECT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionScope) -> str:
    return value


def deserialize_json(data: str) -> ConnectionScope:
    return cast(ConnectionScope, data)
