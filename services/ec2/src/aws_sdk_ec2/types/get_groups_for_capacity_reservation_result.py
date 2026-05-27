"""Generated from Smithy shape ``com.amazonaws.ec2#GetGroupsForCapacityReservationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_group_set
    import aws_sdk_ec2.types.string


class GetGroupsForCapacityReservationResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    capacity_reservation_groups: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_group_set.CapacityReservationGroupSet"
    ]
    """<p>Information about the resource groups to which the Capacity Reservation has been added.</p>"""
