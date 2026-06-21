"""Generated from Smithy shape ``com.amazonaws.kendra#ConditionOperator``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: ConditionOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConditionOperator:
    return cast(ConditionOperator, data)
