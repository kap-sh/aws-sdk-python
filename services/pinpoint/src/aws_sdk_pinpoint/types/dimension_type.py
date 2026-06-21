"""Generated from Smithy shape ``com.amazonaws.pinpoint#DimensionType``."""

from typing import Literal, TypeAlias, cast

DimensionType: TypeAlias = Literal[
    "INCLUSIVE",
    "EXCLUSIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DimensionType) -> str:
    return value


def deserialize_json(data: str) -> DimensionType:
    return cast(DimensionType, data)
