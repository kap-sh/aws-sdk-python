"""Generated from Smithy shape ``com.amazonaws.kendra#ConditionOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

ConditionOperator: TypeAlias = Literal[
    "GreaterThan",
    "GreaterThanOrEquals",
    "LessThan",
    "LessThanOrEquals",
    "Equals",
    "NotEquals",
    "Contains",
    "NotContains",
    "Exists",
    "NotExists",
    "BeginsWith",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GreaterThan",
        "GreaterThanOrEquals",
        "LessThan",
        "LessThanOrEquals",
        "Equals",
        "NotEquals",
        "Contains",
        "NotContains",
        "Exists",
        "NotExists",
        "BeginsWith",
    )
)


def serialize_aws_json_1_1(value: ConditionOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConditionOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConditionOperator value: {data!r}")
    return cast(ConditionOperator, data)
