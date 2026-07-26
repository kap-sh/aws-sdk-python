"""Generated from Smithy shape ``com.amazonaws.appconfig#GrowthType``."""

from typing import Literal, TypeAlias, cast

GrowthType: TypeAlias = Literal[
    "LINEAR",
    "EXPONENTIAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: GrowthType) -> str:
    return value


def deserialize_json(data: str) -> GrowthType:
    return cast(GrowthType, data)
