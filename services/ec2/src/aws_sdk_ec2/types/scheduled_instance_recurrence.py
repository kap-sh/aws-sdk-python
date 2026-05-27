"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstanceRecurrence``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.occurrence_day_set
    import aws_sdk_ec2.types.string


class ScheduledInstanceRecurrence(TypedDict):
    frequency: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The frequency (<code>Daily</code>, <code>Weekly</code>, or <code>Monthly</code>).</p>"""
    interval: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The interval quantity. The interval unit depends on the value of <code>frequency</code>. For example, every 2 weeks or every 2 months.</p>"""
    occurrence_day_set: NotRequired[
        "aws_sdk_ec2.types.occurrence_day_set.OccurrenceDaySet"
    ]
    """<p>The days. For a monthly schedule, this is one or more days of the month (1-31). For a weekly schedule, this is one or more days of the week (1-7, where 1 is Sunday).</p>"""
    occurrence_relative_to_end: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the occurrence is relative to the end of the specified week or month.</p>"""
    occurrence_unit: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The unit for <code>occurrenceDaySet</code> (<code>DayOfWeek</code> or <code>DayOfMonth</code>).</p>"""
