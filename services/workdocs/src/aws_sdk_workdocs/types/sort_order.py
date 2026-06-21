"""Generated from Smithy shape ``com.amazonaws.workdocs#SortOrder``."""

from typing import Literal, TypeAlias, cast

SortOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
def serialize_json(value: SortOrder) -> str:
    return value


def deserialize_json(data: str) -> SortOrder:
    return cast(SortOrder, data)
