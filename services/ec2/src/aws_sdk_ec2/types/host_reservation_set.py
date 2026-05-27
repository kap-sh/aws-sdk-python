"""Generated from Smithy shape ``com.amazonaws.ec2#HostReservationSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.host_reservation

HostReservationSet: TypeAlias = list[
    "aws_sdk_ec2.types.host_reservation.HostReservation"
]
