"""Generated from Smithy shape ``com.amazonaws.rdsdata#TypeHint``."""

from typing import Literal, TypeAlias, cast

TypeHint: TypeAlias = Literal[
    "JSON",
    "UUID",
    "TIMESTAMP",
    "DATE",
    "TIME",
    "DECIMAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: TypeHint) -> str:
    return value


def deserialize_json(data: str) -> TypeHint:
    return cast(TypeHint, data)
