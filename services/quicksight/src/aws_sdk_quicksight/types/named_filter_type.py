"""Generated from Smithy shape ``com.amazonaws.quicksight#NamedFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

NamedFilterType: TypeAlias = Literal[
    "CATEGORY_FILTER",
    "NUMERIC_EQUALITY_FILTER",
    "NUMERIC_RANGE_FILTER",
    "DATE_RANGE_FILTER",
    "RELATIVE_DATE_FILTER",
    "NULL_FILTER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CATEGORY_FILTER",
        "NUMERIC_EQUALITY_FILTER",
        "NUMERIC_RANGE_FILTER",
        "DATE_RANGE_FILTER",
        "RELATIVE_DATE_FILTER",
        "NULL_FILTER",
    )
)


def serialize_json(value: NamedFilterType) -> str:
    return value


def deserialize_json(data: str) -> NamedFilterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NamedFilterType value: {data!r}")
    return cast(NamedFilterType, data)
