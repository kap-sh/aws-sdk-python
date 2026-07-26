"""Generated from Smithy shape ``com.amazonaws.quicksight#PropertyRole``."""

from typing import Literal, TypeAlias, cast

PropertyRole: TypeAlias = Literal[
    "PRIMARY",
    "ID",
]


# --- restJson1 ser/de ---
def serialize_json(value: PropertyRole) -> str:
    return value


def deserialize_json(data: str) -> PropertyRole:
    return cast(PropertyRole, data)
