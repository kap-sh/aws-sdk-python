"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityReservationTopologyResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_topology_set
    import aws_sdk_ec2.types.string


class DescribeCapacityReservationTopologyResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    capacity_reservations: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_topology_set.CapacityReservationTopologySet"
    ]
    """<p>Information about the topology of each Capacity Reservation.</p>"""
