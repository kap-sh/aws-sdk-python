"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ComparisonOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

ComparisonOperator: TypeAlias = Literal[
    "StringEquals",
    "StringNotEquals",
    "StringEqualsIgnoreCase",
    "StringNotEqualsIgnoreCase",
    "StringLike",
    "StringNotLike",
    "NumericEquals",
    "NumericNotEquals",
    "NumericLessThan",
    "NumericLessThanEquals",
    "NumericGreaterThan",
    "NumericGreaterThanEquals",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "StringEquals",
        "StringNotEquals",
        "StringEqualsIgnoreCase",
        "StringNotEqualsIgnoreCase",
        "StringLike",
        "StringNotLike",
        "NumericEquals",
        "NumericNotEquals",
        "NumericLessThan",
        "NumericLessThanEquals",
        "NumericGreaterThan",
        "NumericGreaterThanEquals",
    )
)


def serialize_aws_json_1_0(value: ComparisonOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ComparisonOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComparisonOperator value: {data!r}")
    return cast(ComparisonOperator, data)
