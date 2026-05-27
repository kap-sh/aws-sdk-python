"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesPlacement``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.placement_group_name
    import aws_sdk_ec2.types.string


class ScheduledInstancesPlacement(TypedDict):
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.placement_group_name.PlacementGroupName"]
    """<p>The name of the placement group.</p>"""
