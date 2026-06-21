"""Generated from Smithy shape ``com.amazonaws.datazone#FilterOperator``."""

from typing import Literal, TypeAlias, cast

FilterOperator: TypeAlias = Literal[
    "EQ",
    "LE",
    "LT",
    "GE",
    "GT",
    "TEXT_SEARCH",
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterOperator) -> str:
    return value


def deserialize_json(data: str) -> FilterOperator:
    return cast(FilterOperator, data)
