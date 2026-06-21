"""Generated from Smithy shape ``com.amazonaws.quicksight#CategoryFilterType``."""

from typing import Literal, TypeAlias, cast

CategoryFilterType: TypeAlias = Literal[
    "CUSTOM_FILTER",
    "CUSTOM_FILTER_LIST",
    "FILTER_LIST",
]


# --- restJson1 ser/de ---
def serialize_json(value: CategoryFilterType) -> str:
    return value


def deserialize_json(data: str) -> CategoryFilterType:
    return cast(CategoryFilterType, data)
