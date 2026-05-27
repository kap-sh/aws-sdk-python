"""Generated from Smithy shape ``com.amazonaws.ec2#CreatePlacementGroupResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.placement_group


class CreatePlacementGroupResult(TypedDict):
    placement_group: NotRequired["aws_sdk_ec2.types.placement_group.PlacementGroup"]
    """<p>Information about the placement group.</p>"""
