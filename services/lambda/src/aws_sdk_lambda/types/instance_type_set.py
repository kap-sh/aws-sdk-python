"""Generated from Smithy shape ``com.amazonaws.lambda#InstanceTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.instance_type

InstanceTypeSet: TypeAlias = list["aws_sdk_lambda.types.instance_type.InstanceType"]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceTypeSet) -> list:
    return list(value)


def deserialize_json(data: list) -> InstanceTypeSet:
    return list(data)
