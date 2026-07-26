"""Generated from Smithy shape ``com.amazonaws.connect#SearchContactsMatchType``."""

from typing import Literal, TypeAlias, cast

SearchContactsMatchType: TypeAlias = Literal[
    "MATCH_ALL",
    "MATCH_ANY",
    "MATCH_EXACT",
    "MATCH_NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchContactsMatchType) -> str:
    return value


def deserialize_json(data: str) -> SearchContactsMatchType:
    return cast(SearchContactsMatchType, data)
