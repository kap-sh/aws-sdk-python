"""Generated from Smithy shape ``com.amazonaws.ec2#PlacementGroupIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.placement_group_id

PlacementGroupIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.placement_group_id.PlacementGroupId"
]
