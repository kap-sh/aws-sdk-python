"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstanceRecurrenceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.occurrence_day_request_set
    import aws_sdk_ec2.types.string


class ScheduledInstanceRecurrenceRequest(TypedDict):
    frequency: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The frequency (<code>Daily</code>, <code>Weekly</code>, or <code>Monthly</code>).</p>"""
    interval: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The interval quantity. The interval unit depends on the value of <code>Frequency</code>. For example, every 2 weeks or every 2 months.</p>"""
    occurrence_days: NotRequired[
        "aws_sdk_ec2.types.occurrence_day_request_set.OccurrenceDayRequestSet"
    ]
    """<p>The days. For a monthly schedule, this is one or more days of the month (1-31). For a weekly schedule, this is one or more days of the week (1-7, where 1 is Sunday). You can't specify this value with a daily schedule. If the occurrence is relative to the end of the month, you can specify only a single day.</p>"""
    occurrence_relative_to_end: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the occurrence is relative to the end of the specified week or month. You can't specify this value with a daily schedule.</p>"""
    occurrence_unit: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The unit for <code>OccurrenceDays</code> (<code>DayOfWeek</code> or <code>DayOfMonth</code>). This value is required for a monthly schedule. You can't specify <code>DayOfWeek</code> with a weekly schedule. You can't specify this value with a daily schedule.</p>"""
