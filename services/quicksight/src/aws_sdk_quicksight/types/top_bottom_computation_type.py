"""Generated from Smithy shape ``com.amazonaws.quicksight#TopBottomComputationType``."""

from typing import Literal, TypeAlias, cast

TopBottomComputationType: TypeAlias = Literal[
    "TOP",
    "BOTTOM",
]


# --- restJson1 ser/de ---
def serialize_json(value: TopBottomComputationType) -> str:
    return value


def deserialize_json(data: str) -> TopBottomComputationType:
    return cast(TopBottomComputationType, data)
