"""Generated from Smithy shape ``com.amazonaws.costexplorer#NumericOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

NumericOperator: TypeAlias = Literal[
    "EQUAL",
    "GREATER_THAN_OR_EQUAL",
    "LESS_THAN_OR_EQUAL",
    "GREATER_THAN",
    "LESS_THAN",
    "BETWEEN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUAL",
        "GREATER_THAN_OR_EQUAL",
        "LESS_THAN_OR_EQUAL",
        "GREATER_THAN",
        "LESS_THAN",
        "BETWEEN",
    )
)


def serialize_aws_json_1_1(value: NumericOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NumericOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NumericOperator value: {data!r}")
    return cast(NumericOperator, data)
