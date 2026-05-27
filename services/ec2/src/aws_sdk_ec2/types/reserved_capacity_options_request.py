"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedCapacityOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reservation_type_list_request


class ReservedCapacityOptionsRequest(TypedDict):
    reservation_types: NotRequired[
        "aws_sdk_ec2.types.reservation_type_list_request.ReservationTypeListRequest"
    ]
    """<p>The types of Capacity Reservations to use for fulfilling the EC2 Fleet request.</p>"""
