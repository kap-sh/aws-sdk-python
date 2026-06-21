"""Generated from Smithy shape ``com.amazonaws.datasync#Operator``."""

from typing import Literal, TypeAlias, cast

Operator: TypeAlias = Literal[
    "Equals",
    "NotEquals",
    "In",
    "LessThanOrEqual",
    "LessThan",
    "GreaterThanOrEqual",
    "GreaterThan",
    "Contains",
    "NotContains",
    "BeginsWith",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Operator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Operator:
    return cast(Operator, data)
