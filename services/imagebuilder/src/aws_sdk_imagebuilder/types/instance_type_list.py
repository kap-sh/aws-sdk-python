"""Generated from Smithy shape ``com.amazonaws.imagebuilder#InstanceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.instance_type

InstanceTypeList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.instance_type.InstanceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> InstanceTypeList:
    return list(data)
