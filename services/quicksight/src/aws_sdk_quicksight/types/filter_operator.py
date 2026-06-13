"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

FilterOperator: TypeAlias = Literal[
    "StringEquals",
    "StringLike",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "StringEquals",
        "StringLike",
    )
)


def serialize_json(value: FilterOperator) -> str:
    return value


def deserialize_json(data: str) -> FilterOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterOperator value: {data!r}")
    return cast(FilterOperator, data)
