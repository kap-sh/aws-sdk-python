"""Generated from Smithy shape ``com.amazonaws.ec2#MoveCapacityReservationInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation
    import aws_sdk_ec2.types.integer


class MoveCapacityReservationInstancesResult(TypedDict):
    source_capacity_reservation: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation.CapacityReservation"
    ]
    """<p> Information about the source Capacity Reservation. </p>"""
    destination_capacity_reservation: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation.CapacityReservation"
    ]
    """<p> Information about the destination Capacity Reservation. </p>"""
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p> The number of instances that were moved from the source Capacity Reservation to the destination Capacity Reservation. </p>"""
