"""Generated from Smithy shape ``com.amazonaws.backup#Index``."""

from typing import Literal, TypeAlias, cast

Index: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Index) -> str:
    return value


def deserialize_json(data: str) -> Index:
    return cast(Index, data)
