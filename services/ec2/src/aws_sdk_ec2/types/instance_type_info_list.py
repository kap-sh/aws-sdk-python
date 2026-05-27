"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceTypeInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_type_info

InstanceTypeInfoList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_type_info.InstanceTypeInfo"
]
