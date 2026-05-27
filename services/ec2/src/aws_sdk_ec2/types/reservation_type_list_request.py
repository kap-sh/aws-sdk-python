"""Generated from Smithy shape ``com.amazonaws.ec2#ReservationTypeListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_reservation_type

ReservationTypeListRequest: TypeAlias = list[
    "aws_sdk_ec2.types.fleet_reservation_type.FleetReservationType"
]
