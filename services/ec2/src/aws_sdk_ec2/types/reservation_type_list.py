"""Generated from Smithy shape ``com.amazonaws.ec2#ReservationTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_reservation_type

ReservationTypeList: TypeAlias = list[
    "aws_sdk_ec2.types.fleet_reservation_type.FleetReservationType"
]
