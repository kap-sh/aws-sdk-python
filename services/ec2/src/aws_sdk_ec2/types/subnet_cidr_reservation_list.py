"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetCidrReservationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.subnet_cidr_reservation

SubnetCidrReservationList: TypeAlias = list[
    "aws_sdk_ec2.types.subnet_cidr_reservation.SubnetCidrReservation"
]
