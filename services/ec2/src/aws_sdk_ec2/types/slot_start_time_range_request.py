"""Generated from Smithy shape ``com.amazonaws.ec2#SlotStartTimeRangeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time


class SlotStartTimeRangeRequest(TypedDict):
    earliest_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The earliest date and time, in UTC, for the Scheduled Instance to start.</p>"""
    latest_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The latest date and time, in UTC, for the Scheduled Instance to start.</p>"""
