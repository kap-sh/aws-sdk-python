"""Generated from Smithy shape ``com.amazonaws.quicksight#LegendPosition``."""

from typing import Literal, TypeAlias, cast

LegendPosition: TypeAlias = Literal[
    "AUTO",
    "RIGHT",
    "BOTTOM",
    "TOP",
]


# --- restJson1 ser/de ---
def serialize_json(value: LegendPosition) -> str:
    return value


def deserialize_json(data: str) -> LegendPosition:
    return cast(LegendPosition, data)
