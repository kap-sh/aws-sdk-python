"""Generated from Smithy shape ``com.amazonaws.quicksight#ComparisonMethod``."""

from typing import Literal, TypeAlias, cast

ComparisonMethod: TypeAlias = Literal[
    "DIFFERENCE",
    "PERCENT_DIFFERENCE",
    "PERCENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComparisonMethod) -> str:
    return value


def deserialize_json(data: str) -> ComparisonMethod:
    return cast(ComparisonMethod, data)
