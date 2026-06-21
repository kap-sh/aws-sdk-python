"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SearchOrder``."""

from typing import Literal, TypeAlias, cast

SearchOrder: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchOrder) -> str:
    return value


def deserialize_json(data: str) -> SearchOrder:
    return cast(SearchOrder, data)
