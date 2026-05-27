"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstanceAvailability``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.scheduled_instance_recurrence
    import aws_sdk_ec2.types.string


class ScheduledInstanceAvailability(TypedDict):
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    available_instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of available instances.</p>"""
    first_slot_start_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time period for the first schedule to start.</p>"""
    hourly_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The hourly price for a single instance.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance type. You can specify one of the C3, C4, M4, or R3 instance types.</p>"""
    max_term_duration_in_days: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum term. The only possible value is 365 days.</p>"""
    min_term_duration_in_days: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The minimum term. The only possible value is 365 days.</p>"""
    network_platform: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The network platform.</p>"""
    platform: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The platform (<code>Linux/UNIX</code> or <code>Windows</code>).</p>"""
    purchase_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The purchase token. This token expires in two hours.</p>"""
    recurrence: NotRequired[
        "aws_sdk_ec2.types.scheduled_instance_recurrence.ScheduledInstanceRecurrence"
    ]
    """<p>The schedule recurrence.</p>"""
    slot_duration_in_hours: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of hours in the schedule.</p>"""
    total_scheduled_instance_hours: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The total number of hours for a single instance for the entire term.</p>"""
