"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_id
    import aws_sdk_ec2.types.integer


class CapacityReservationStatus(TypedDict):
    capacity_reservation_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p>The ID of the Capacity Reservation.</p>"""
    total_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The combined amount of <code>Available</code> and <code>Unavailable</code> capacity in the Capacity Reservation.</p>"""
    total_available_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The remaining capacity. Indicates the amount of resources that can be launched into the Capacity Reservation.</p>"""
    total_unavailable_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The used capacity. Indicates that the capacity is in use by resources that are running in the Capacity Reservation.</p>"""
