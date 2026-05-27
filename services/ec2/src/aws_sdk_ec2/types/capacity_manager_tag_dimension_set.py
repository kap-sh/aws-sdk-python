"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerTagDimensionSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_tag_dimension

CapacityManagerTagDimensionSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_manager_tag_dimension.CapacityManagerTagDimension"
]
