"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualRole``."""

from typing import Literal, TypeAlias, cast

VisualRole: TypeAlias = Literal[
    "PRIMARY",
    "COMPLIMENTARY",
    "MULTI_INTENT",
    "FALLBACK",
    "FRAGMENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: VisualRole) -> str:
    return value


def deserialize_json(data: str) -> VisualRole:
    return cast(VisualRole, data)
