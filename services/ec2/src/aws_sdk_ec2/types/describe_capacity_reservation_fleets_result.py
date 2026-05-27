"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityReservationFleetsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_fleet_set
    import aws_sdk_ec2.types.string


class DescribeCapacityReservationFleetsResult(TypedDict):
    capacity_reservation_fleets: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_fleet_set.CapacityReservationFleetSet"
    ]
    """<p>Information about the Capacity Reservation Fleets.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
