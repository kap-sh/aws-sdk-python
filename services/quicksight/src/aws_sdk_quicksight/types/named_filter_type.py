"""Generated from Smithy shape ``com.amazonaws.quicksight#NamedFilterType``."""

from typing import Literal, TypeAlias, cast

NamedFilterType: TypeAlias = Literal[
    "CATEGORY_FILTER",
    "NUMERIC_EQUALITY_FILTER",
    "NUMERIC_RANGE_FILTER",
    "DATE_RANGE_FILTER",
    "RELATIVE_DATE_FILTER",
    "NULL_FILTER",
]


# --- restJson1 ser/de ---
def serialize_json(value: NamedFilterType) -> str:
    return value


def deserialize_json(data: str) -> NamedFilterType:
    return cast(NamedFilterType, data)
