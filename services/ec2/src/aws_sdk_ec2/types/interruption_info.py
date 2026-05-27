"""Generated from Smithy shape ``com.amazonaws.ec2#InterruptionInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.interruption_type
    import aws_sdk_ec2.types.string


class InterruptionInfo(TypedDict):
    source_capacity_reservation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The ID of the source Capacity Reservation from which the interruptible reservation was created. </p>"""
    interruption_type: NotRequired[
        "aws_sdk_ec2.types.interruption_type.InterruptionType"
    ]
    """<p> The interruption type that determines how instances are terminated when capacity is reclaimed. </p>"""
