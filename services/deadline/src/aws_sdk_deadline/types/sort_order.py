"""Generated from Smithy shape ``com.amazonaws.deadline#SortOrder``."""

from typing import Literal, TypeAlias, cast

SortOrder: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: SortOrder) -> str:
    return value


def deserialize_json(data: str) -> SortOrder:
    return cast(SortOrder, data)
