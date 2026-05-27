"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedCapacityOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reservation_type_list


class ReservedCapacityOptions(TypedDict):
    reservation_types: NotRequired[
        "aws_sdk_ec2.types.reservation_type_list.ReservationTypeList"
    ]
    """<p>The types of Capacity Reservations used for fulfilling the EC2 Fleet request.</p>"""
