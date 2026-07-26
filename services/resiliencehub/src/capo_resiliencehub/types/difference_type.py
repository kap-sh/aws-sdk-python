"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DifferenceType``."""

from typing import Literal, TypeAlias, cast

DifferenceType: TypeAlias = Literal[
    "NotEqual",
    "Added",
    "Removed",
]


# --- restJson1 ser/de ---
def serialize_json(value: DifferenceType) -> str:
    return value


def deserialize_json(data: str) -> DifferenceType:
    return cast(DifferenceType, data)
