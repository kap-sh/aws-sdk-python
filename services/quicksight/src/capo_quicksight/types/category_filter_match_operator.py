"""Generated from Smithy shape ``com.amazonaws.quicksight#CategoryFilterMatchOperator``."""

from typing import Literal, TypeAlias, cast

CategoryFilterMatchOperator: TypeAlias = Literal[
    "EQUALS",
    "DOES_NOT_EQUAL",
    "CONTAINS",
    "DOES_NOT_CONTAIN",
    "STARTS_WITH",
    "ENDS_WITH",
]


# --- restJson1 ser/de ---
def serialize_json(value: CategoryFilterMatchOperator) -> str:
    return value


def deserialize_json(data: str) -> CategoryFilterMatchOperator:
    return cast(CategoryFilterMatchOperator, data)
