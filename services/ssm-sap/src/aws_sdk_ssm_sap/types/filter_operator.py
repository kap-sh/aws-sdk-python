"""Generated from Smithy shape ``com.amazonaws.ssmsap#FilterOperator``."""

from typing import Literal, TypeAlias, cast

FilterOperator: TypeAlias = Literal[
    "Equals",
    "GreaterThanOrEquals",
    "LessThanOrEquals",
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterOperator) -> str:
    return value


def deserialize_json(data: str) -> FilterOperator:
    return cast(FilterOperator, data)
