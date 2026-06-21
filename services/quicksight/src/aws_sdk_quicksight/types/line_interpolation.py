"""Generated from Smithy shape ``com.amazonaws.quicksight#LineInterpolation``."""

from typing import Literal, TypeAlias, cast

LineInterpolation: TypeAlias = Literal[
    "LINEAR",
    "SMOOTH",
    "STEPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: LineInterpolation) -> str:
    return value


def deserialize_json(data: str) -> LineInterpolation:
    return cast(LineInterpolation, data)
