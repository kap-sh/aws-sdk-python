"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceEventWindowTimeRangeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.hour
    import aws_sdk_ec2.types.week_day


class InstanceEventWindowTimeRangeRequest(TypedDict):
    start_week_day: NotRequired["aws_sdk_ec2.types.week_day.WeekDay"]
    """<p>The day on which the time range begins.</p>"""
    start_hour: NotRequired["aws_sdk_ec2.types.hour.Hour"]
    """<p>The hour when the time range begins.</p>"""
    end_week_day: NotRequired["aws_sdk_ec2.types.week_day.WeekDay"]
    """<p>The day on which the time range ends.</p>"""
    end_hour: NotRequired["aws_sdk_ec2.types.hour.Hour"]
    """<p>The hour when the time range ends.</p>"""
