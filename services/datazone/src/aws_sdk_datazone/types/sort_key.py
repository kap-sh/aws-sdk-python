"""Generated from Smithy shape ``com.amazonaws.datazone#SortKey``."""

from typing import Literal, TypeAlias, cast

SortKey: TypeAlias = Literal[
    "CREATED_AT",
    "UPDATED_AT",
]


# --- restJson1 ser/de ---
def serialize_json(value: SortKey) -> str:
    return value


def deserialize_json(data: str) -> SortKey:
    return cast(SortKey, data)
