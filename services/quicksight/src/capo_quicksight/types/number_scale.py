"""Generated from Smithy shape ``com.amazonaws.quicksight#NumberScale``."""

from typing import Literal, TypeAlias, cast

NumberScale: TypeAlias = Literal[
    "NONE",
    "AUTO",
    "THOUSANDS",
    "MILLIONS",
    "BILLIONS",
    "TRILLIONS",
    "LAKHS",
    "CRORES",
]


# --- restJson1 ser/de ---
def serialize_json(value: NumberScale) -> str:
    return value


def deserialize_json(data: str) -> NumberScale:
    return cast(NumberScale, data)
