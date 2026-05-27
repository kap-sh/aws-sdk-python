"""Generated from Smithy shape ``com.amazonaws.ec2#ExcludedInstanceTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.excluded_instance_type

ExcludedInstanceTypeSet: TypeAlias = list[
    "aws_sdk_ec2.types.excluded_instance_type.ExcludedInstanceType"
]
