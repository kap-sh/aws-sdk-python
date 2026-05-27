"""Generated from Smithy shape ``com.amazonaws.ec2#DescribePlacementGroupsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.placement_group_list


class DescribePlacementGroupsResult(TypedDict):
    placement_groups: NotRequired[
        "aws_sdk_ec2.types.placement_group_list.PlacementGroupList"
    ]
    """<p>Information about the placement groups.</p>"""
