"""Generated from Smithy shape ``com.amazonaws.ec2#ReservationValue``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class ReservationValue(TypedDict):
    hourly_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The hourly rate of the reservation.</p>"""
    remaining_total_value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The balance of the total value (the sum of remainingUpfrontValue + hourlyPrice * number of hours remaining).</p>"""
    remaining_upfront_value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The remaining upfront cost of the reservation.</p>"""
