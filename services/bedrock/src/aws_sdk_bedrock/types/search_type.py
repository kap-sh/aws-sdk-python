"""Generated from Smithy shape ``com.amazonaws.bedrock#SearchType``."""

from typing import Literal, TypeAlias, cast

SearchType: TypeAlias = Literal[
    "HYBRID",
    "SEMANTIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchType) -> str:
    return value


def deserialize_json(data: str) -> SearchType:
    return cast(SearchType, data)
