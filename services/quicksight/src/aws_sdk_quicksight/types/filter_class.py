"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

FilterClass: TypeAlias = Literal[
    "ENFORCED_VALUE_FILTER",
    "CONDITIONAL_VALUE_FILTER",
    "NAMED_VALUE_FILTER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENFORCED_VALUE_FILTER",
        "CONDITIONAL_VALUE_FILTER",
        "NAMED_VALUE_FILTER",
    )
)


def serialize_json(value: FilterClass) -> str:
    return value


def deserialize_json(data: str) -> FilterClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterClass value: {data!r}")
    return cast(FilterClass, data)
