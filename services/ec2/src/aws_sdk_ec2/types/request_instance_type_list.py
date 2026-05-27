"""Generated from Smithy shape ``com.amazonaws.ec2#RequestInstanceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_type

RequestInstanceTypeList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_type.InstanceType"
]
