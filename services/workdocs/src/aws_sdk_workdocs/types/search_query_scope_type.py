"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchQueryScopeType``."""

from typing import Literal, TypeAlias, cast

SearchQueryScopeType: TypeAlias = Literal[
    "NAME",
    "CONTENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchQueryScopeType) -> str:
    return value


def deserialize_json(data: str) -> SearchQueryScopeType:
    return cast(SearchQueryScopeType, data)
