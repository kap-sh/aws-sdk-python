"""Generated from Smithy shape ``com.amazonaws.ec2#AllowedInstanceTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allowed_instance_type

AllowedInstanceTypeSet: TypeAlias = list[
    "aws_sdk_ec2.types.allowed_instance_type.AllowedInstanceType"
]
