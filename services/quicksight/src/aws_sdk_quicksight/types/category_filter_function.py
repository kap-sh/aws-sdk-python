"""Generated from Smithy shape ``com.amazonaws.quicksight#CategoryFilterFunction``."""

from typing import Literal, TypeAlias, cast

CategoryFilterFunction: TypeAlias = Literal[
    "EXACT",
    "CONTAINS",
]


# --- restJson1 ser/de ---
def serialize_json(value: CategoryFilterFunction) -> str:
    return value


def deserialize_json(data: str) -> CategoryFilterFunction:
    return cast(CategoryFilterFunction, data)
