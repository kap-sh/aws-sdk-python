"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#SortDirection``."""

from typing import Literal, TypeAlias, cast

SortDirection: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
def serialize_json(value: SortDirection) -> str:
    return value


def deserialize_json(data: str) -> SortDirection:
    return cast(SortDirection, data)
