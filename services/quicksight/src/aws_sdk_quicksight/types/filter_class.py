"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterClass``."""

from typing import Literal, TypeAlias, cast

FilterClass: TypeAlias = Literal[
    "ENFORCED_VALUE_FILTER",
    "CONDITIONAL_VALUE_FILTER",
    "NAMED_VALUE_FILTER",
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterClass) -> str:
    return value


def deserialize_json(data: str) -> FilterClass:
    return cast(FilterClass, data)
