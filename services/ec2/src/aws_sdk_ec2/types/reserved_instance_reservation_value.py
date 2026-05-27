"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstanceReservationValue``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reservation_value
    import aws_sdk_ec2.types.string


class ReservedInstanceReservationValue(TypedDict):
    reservation_value: NotRequired[
        "aws_sdk_ec2.types.reservation_value.ReservationValue"
    ]
    """<p>The total value of the Convertible Reserved Instance that you are exchanging.</p>"""
    reserved_instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Convertible Reserved Instance that you are exchanging.</p>"""
