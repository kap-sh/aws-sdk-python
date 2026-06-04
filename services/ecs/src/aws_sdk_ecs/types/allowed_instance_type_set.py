"""Generated from Smithy shape ``com.amazonaws.ecs#AllowedInstanceTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.allowed_instance_type

AllowedInstanceTypeSet: TypeAlias = list[
    "aws_sdk_ecs.types.allowed_instance_type.AllowedInstanceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllowedInstanceTypeSet) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AllowedInstanceTypeSet:
    return list(data)
