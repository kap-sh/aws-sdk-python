"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeScheduledInstanceAvailabilityRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_scheduled_instance_availability_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.scheduled_instance_recurrence_request
    import aws_sdk_ec2.types.slot_date_time_range_request
    import aws_sdk_ec2.types.string


class DescribeScheduledInstanceAvailabilityRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>availability-zone</code> - The Availability Zone (for example, <code>us-west-2a</code>).</p> </li> <li> <p> <code>instance-type</code> - The instance type (for example, <code>c4.large</code>).</p> </li> <li> <p> <code>platform</code> - The platform (<code>Linux/UNIX</code> or <code>Windows</code>).</p> </li> </ul>"""
    first_slot_start_time_range: NotRequired[
        "aws_sdk_ec2.types.slot_date_time_range_request.SlotDateTimeRangeRequest"
    ]
    """<p>The time period for the first schedule to start.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_scheduled_instance_availability_max_results.DescribeScheduledInstanceAvailabilityMaxResults"
    ]
    """<p>The maximum number of results to return in a single call. This value can be between 5 and 300. The default value is 300. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>"""
    max_slot_duration_in_hours: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum available duration, in hours. This value must be greater than <code>MinSlotDurationInHours</code> and less than 1,720.</p>"""
    min_slot_duration_in_hours: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The minimum available duration, in hours. The minimum required duration is 1,200 hours per year. For example, the minimum daily schedule is 4 hours, the minimum weekly schedule is 24 hours, and the minimum monthly schedule is 100 hours.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next set of results.</p>"""
    recurrence: NotRequired[
        "aws_sdk_ec2.types.scheduled_instance_recurrence_request.ScheduledInstanceRecurrenceRequest"
    ]
    """<p>The schedule recurrence.</p>"""
