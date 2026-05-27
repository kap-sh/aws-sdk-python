"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityReservationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_set
    import aws_sdk_ec2.types.string


class DescribeCapacityReservationsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    capacity_reservations: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_set.CapacityReservationSet"
    ]
    """<p>Information about the Capacity Reservations.</p>"""
