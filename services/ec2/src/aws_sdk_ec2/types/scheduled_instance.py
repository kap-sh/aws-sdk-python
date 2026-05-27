"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstance``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.scheduled_instance_recurrence
    import aws_sdk_ec2.types.string


class ScheduledInstance(TypedDict):
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    create_date: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date when the Scheduled Instance was purchased.</p>"""
    hourly_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The hourly price for a single instance.</p>"""
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance type.</p>"""
    network_platform: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The network platform.</p>"""
    next_slot_start_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time for the next schedule to start.</p>"""
    platform: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The platform (<code>Linux/UNIX</code> or <code>Windows</code>).</p>"""
    previous_slot_end_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time that the previous schedule ended or will end.</p>"""
    recurrence: NotRequired[
        "aws_sdk_ec2.types.scheduled_instance_recurrence.ScheduledInstanceRecurrence"
    ]
    """<p>The schedule recurrence.</p>"""
    scheduled_instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Scheduled Instance ID.</p>"""
    slot_duration_in_hours: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of hours in the schedule.</p>"""
    term_end_date: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The end date for the Scheduled Instance.</p>"""
    term_start_date: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The start date for the Scheduled Instance.</p>"""
    total_scheduled_instance_hours: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The total number of hours for a single instance for the entire term.</p>"""
