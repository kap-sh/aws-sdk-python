"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCapacityReservationBySplittingResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation
    import aws_sdk_ec2.types.integer


class CreateCapacityReservationBySplittingResult(TypedDict):
    source_capacity_reservation: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation.CapacityReservation"
    ]
    """<p> Information about the source Capacity Reservation. </p>"""
    destination_capacity_reservation: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation.CapacityReservation"
    ]
    """<p> Information about the destination Capacity Reservation. </p>"""
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p> The number of instances in the new Capacity Reservation. The number of instances in the source Capacity Reservation was reduced by this amount. </p>"""
