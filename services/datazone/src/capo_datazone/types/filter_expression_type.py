"""Generated from Smithy shape ``com.amazonaws.datazone#FilterExpressionType``."""

from typing import Literal, TypeAlias, cast

FilterExpressionType: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterExpressionType) -> str:
    return value


def deserialize_json(data: str) -> FilterExpressionType:
    return cast(FilterExpressionType, data)
