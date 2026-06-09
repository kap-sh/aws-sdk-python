"""Generated from Smithy shape ``com.amazonaws.dynamodb#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb.errors import DeserializationError

ComparisonOperator: TypeAlias = Literal[
    "EQ",
    "NE",
    "IN",
    "LE",
    "LT",
    "GE",
    "GT",
    "BETWEEN",
    "NOT_NULL",
    "NULL",
    "CONTAINS",
    "NOT_CONTAINS",
    "BEGINS_WITH",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQ",
        "NE",
        "IN",
        "LE",
        "LT",
        "GE",
        "GT",
        "BETWEEN",
        "NOT_NULL",
        "NULL",
        "CONTAINS",
        "NOT_CONTAINS",
        "BEGINS_WITH",
    )
)


def serialize_aws_json_1_0(value: ComparisonOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ComparisonOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComparisonOperator value: {data!r}")
    return cast(ComparisonOperator, data)
