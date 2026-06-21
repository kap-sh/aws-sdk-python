"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterVisualScope``."""

from typing import Literal, TypeAlias, cast

FilterVisualScope: TypeAlias = Literal[
    "ALL_VISUALS",
    "SELECTED_VISUALS",
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterVisualScope) -> str:
    return value


def deserialize_json(data: str) -> FilterVisualScope:
    return cast(FilterVisualScope, data)
