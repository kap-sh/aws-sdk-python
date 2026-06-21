"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchCollectionType``."""

from typing import Literal, TypeAlias, cast

SearchCollectionType: TypeAlias = Literal[
    "OWNED",
    "SHARED_WITH_ME",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchCollectionType) -> str:
    return value


def deserialize_json(data: str) -> SearchCollectionType:
    return cast(SearchCollectionType, data)
