"""Generated from Smithy shape ``com.amazonaws.quicksight#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ComparisonOperator: TypeAlias = Literal[
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


def serialize_json(value: ComparisonOperator) -> str:
    return value


def deserialize_json(data: str) -> ComparisonOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComparisonOperator value: {data!r}")
    return cast(ComparisonOperator, data)
