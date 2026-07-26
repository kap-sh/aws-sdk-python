"""Generated from Smithy shape ``com.amazonaws.pinpoint#Type``."""

from typing import Literal, TypeAlias, cast

Type: TypeAlias = Literal[
    "ALL",
    "ANY",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Type) -> str:
    return value


def deserialize_json(data: str) -> Type:
    return cast(Type, data)
