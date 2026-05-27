"""Generated from Smithy shape ``com.amazonaws.ec2#PlacementGroupStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.placement_group_name

PlacementGroupStringList: TypeAlias = list[
    "aws_sdk_ec2.types.placement_group_name.PlacementGroupName"
]
