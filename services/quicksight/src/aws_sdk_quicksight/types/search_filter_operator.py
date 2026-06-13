"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SearchFilterOperator: TypeAlias = Literal[
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


def serialize_json(value: SearchFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> SearchFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchFilterOperator value: {data!r}")
    return cast(SearchFilterOperator, data)
