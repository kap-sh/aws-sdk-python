"""Generated from Smithy shape ``com.amazonaws.quicksight#PropertyUsage``."""

from typing import Literal, TypeAlias, cast

PropertyUsage: TypeAlias = Literal[
    "INHERIT",
    "DIMENSION",
    "MEASURE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PropertyUsage) -> str:
    return value


def deserialize_json(data: str) -> PropertyUsage:
    return cast(PropertyUsage, data)
