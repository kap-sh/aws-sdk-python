"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSubnetCidrReservationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.subnet_cidr_reservation


class CreateSubnetCidrReservationResult(TypedDict):
    subnet_cidr_reservation: NotRequired[
        "aws_sdk_ec2.types.subnet_cidr_reservation.SubnetCidrReservation"
    ]
    """<p>Information about the created subnet CIDR reservation.</p>"""
