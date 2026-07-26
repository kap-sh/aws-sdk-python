"""Generated from Smithy shape ``com.amazonaws.groundstation#AngleUnits``."""

from typing import Literal, TypeAlias, cast

AngleUnits: TypeAlias = Literal[
    "DEGREE_ANGLE",
    "RADIAN",
]


# --- restJson1 ser/de ---
def serialize_json(value: AngleUnits) -> str:
    return value


def deserialize_json(data: str) -> AngleUnits:
    return cast(AngleUnits, data)
