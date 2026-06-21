"""Generated from Smithy shape ``com.amazonaws.deadline#SearchTermMatchingType``."""

from typing import Literal, TypeAlias, cast

SearchTermMatchingType: TypeAlias = Literal[
    "FUZZY_MATCH",
    "CONTAINS",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchTermMatchingType) -> str:
    return value


def deserialize_json(data: str) -> SearchTermMatchingType:
    return cast(SearchTermMatchingType, data)
