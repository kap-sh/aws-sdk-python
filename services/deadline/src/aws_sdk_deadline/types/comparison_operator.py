"""Generated from Smithy shape ``com.amazonaws.deadline#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

ComparisonOperator: TypeAlias = Literal[
    "EQUAL",
    "NOT_EQUAL",
    "GREATER_THAN_EQUAL_TO",
    "GREATER_THAN",
    "LESS_THAN_EQUAL_TO",
    "LESS_THAN",
    "ANY_EQUALS",
    "ALL_NOT_EQUALS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUAL",
        "NOT_EQUAL",
        "GREATER_THAN_EQUAL_TO",
        "GREATER_THAN",
        "LESS_THAN_EQUAL_TO",
        "LESS_THAN",
        "ANY_EQUALS",
        "ALL_NOT_EQUALS",
    )
)


def serialize_json(value: ComparisonOperator) -> str:
    return value


def deserialize_json(data: str) -> ComparisonOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComparisonOperator value: {data!r}")
    return cast(ComparisonOperator, data)
