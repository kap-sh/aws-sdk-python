"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeScheduledInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.scheduled_instance_id_request_set
    import aws_sdk_ec2.types.slot_start_time_range_request
    import aws_sdk_ec2.types.string


class DescribeScheduledInstancesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>availability-zone</code> - The Availability Zone (for example, <code>us-west-2a</code>).</p> </li> <li> <p> <code>instance-type</code> - The instance type (for example, <code>c4.large</code>).</p> </li> <li> <p> <code>platform</code> - The platform (<code>Linux/UNIX</code> or <code>Windows</code>).</p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of results to return in a single call. This value can be between 5 and 300. The default value is 100. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next set of results.</p>"""
    scheduled_instance_ids: NotRequired[
        "aws_sdk_ec2.types.scheduled_instance_id_request_set.ScheduledInstanceIdRequestSet"
    ]
    """<p>The Scheduled Instance IDs.</p>"""
    slot_start_time_range: NotRequired[
        "aws_sdk_ec2.types.slot_start_time_range_request.SlotStartTimeRangeRequest"
    ]
    """<p>The time period for the first schedule to start.</p>"""
