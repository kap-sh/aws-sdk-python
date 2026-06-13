"""Generated from Smithy shape ``com.amazonaws.quicksight#CategoryFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

CategoryFilterType: TypeAlias = Literal[
    "CUSTOM_FILTER",
    "CUSTOM_FILTER_LIST",
    "FILTER_LIST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOM_FILTER",
        "CUSTOM_FILTER_LIST",
        "FILTER_LIST",
    )
)


def serialize_json(value: CategoryFilterType) -> str:
    return value


def deserialize_json(data: str) -> CategoryFilterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CategoryFilterType value: {data!r}")
    return cast(CategoryFilterType, data)
