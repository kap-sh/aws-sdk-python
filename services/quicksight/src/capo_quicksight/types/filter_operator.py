"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterOperator``."""

from typing import Literal, TypeAlias, cast

FilterOperator: TypeAlias = Literal[
    "StringEquals",
    "StringLike",
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterOperator) -> str:
    return value


def deserialize_json(data: str) -> FilterOperator:
    return cast(FilterOperator, data)
