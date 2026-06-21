"""Generated from Smithy shape ``com.amazonaws.quicksight#BarsArrangement``."""

from typing import Literal, TypeAlias, cast

BarsArrangement: TypeAlias = Literal[
    "CLUSTERED",
    "STACKED",
    "STACKED_PERCENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: BarsArrangement) -> str:
    return value


def deserialize_json(data: str) -> BarsArrangement:
    return cast(BarsArrangement, data)
