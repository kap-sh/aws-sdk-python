"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationCommitmentInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time


class CapacityReservationCommitmentInfo(TypedDict):
    committed_instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The instance capacity that you committed to when you requested the future-dated Capacity Reservation.</p>"""
    commitment_end_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the commitment duration expires, in the ISO8601 format in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>). You can't decrease the instance count or cancel the Capacity Reservation before this date and time.</p>"""
