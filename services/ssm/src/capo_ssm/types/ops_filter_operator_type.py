"""Generated from Smithy shape ``com.amazonaws.ssm#OpsFilterOperatorType``."""

from typing import Literal, TypeAlias, cast

OpsFilterOperatorType: TypeAlias = Literal[
    "Equal",
    "NotEqual",
    "BeginWith",
    "LessThan",
    "GreaterThan",
    "Exists",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsFilterOperatorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpsFilterOperatorType:
    return cast(OpsFilterOperatorType, data)
