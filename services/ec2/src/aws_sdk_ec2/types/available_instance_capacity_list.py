"""Generated from Smithy shape ``com.amazonaws.ec2#AvailableInstanceCapacityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_capacity

AvailableInstanceCapacityList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_capacity.InstanceCapacity"
]
