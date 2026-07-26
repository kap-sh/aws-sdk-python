"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchFilterOperator``."""

from typing import Literal, TypeAlias, cast

SearchFilterOperator: TypeAlias = Literal[
    "StringEquals",
    "StringLike",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> SearchFilterOperator:
    return cast(SearchFilterOperator, data)
