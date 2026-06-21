"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AttributeDimensionType``."""

from typing import Literal, TypeAlias, cast

AttributeDimensionType: TypeAlias = Literal[
    "INCLUSIVE",
    "EXCLUSIVE",
    "CONTAINS",
    "BEGINS_WITH",
    "ENDS_WITH",
    "BEFORE",
    "AFTER",
    "BETWEEN",
    "NOT_BETWEEN",
    "ON",
    "GREATER_THAN",
    "LESS_THAN",
    "GREATER_THAN_OR_EQUAL",
    "LESS_THAN_OR_EQUAL",
    "EQUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeDimensionType) -> str:
    return value


def deserialize_json(data: str) -> AttributeDimensionType:
    return cast(AttributeDimensionType, data)
