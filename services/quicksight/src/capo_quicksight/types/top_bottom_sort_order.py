"""Generated from Smithy shape ``com.amazonaws.quicksight#TopBottomSortOrder``."""

from typing import Literal, TypeAlias, cast

TopBottomSortOrder: TypeAlias = Literal[
    "PERCENT_DIFFERENCE",
    "ABSOLUTE_DIFFERENCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TopBottomSortOrder) -> str:
    return value


def deserialize_json(data: str) -> TopBottomSortOrder:
    return cast(TopBottomSortOrder, data)
