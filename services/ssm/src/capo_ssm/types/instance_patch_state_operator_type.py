"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePatchStateOperatorType``."""

from typing import Literal, TypeAlias, cast

InstancePatchStateOperatorType: TypeAlias = Literal[
    "Equal",
    "NotEqual",
    "LessThan",
    "GreaterThan",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePatchStateOperatorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstancePatchStateOperatorType:
    return cast(InstancePatchStateOperatorType, data)
