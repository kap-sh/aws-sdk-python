"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SearchType``."""

from typing import Literal, TypeAlias, cast

SearchType: TypeAlias = Literal["SEMANTIC",]


# --- restJson1 ser/de ---
def serialize_json(value: SearchType) -> str:
    return value


def deserialize_json(data: str) -> SearchType:
    return cast(SearchType, data)
