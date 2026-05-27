"""Generated from Smithy shape ``com.amazonaws.ec2#PlacementResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.placement_group_name


class PlacementResponse(TypedDict):
    group_name: NotRequired["aws_sdk_ec2.types.placement_group_name.PlacementGroupName"]
    """<p>The name of the placement group that the instance is in.</p>"""
