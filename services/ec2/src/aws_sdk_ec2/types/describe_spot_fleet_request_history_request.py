"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotFleetRequestHistoryRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.describe_spot_fleet_request_history_max_results
    import aws_sdk_ec2.types.event_type
    import aws_sdk_ec2.types.spot_fleet_request_id
    import aws_sdk_ec2.types.string


class DescribeSpotFleetRequestHistoryRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    spot_fleet_request_id: NotRequired[
        "aws_sdk_ec2.types.spot_fleet_request_id.SpotFleetRequestId"
    ]
    """<p>The ID of the Spot Fleet request.</p>"""
    event_type: NotRequired["aws_sdk_ec2.types.event_type.EventType"]
    """<p>The type of events to describe. By default, all events are described.</p>"""
    start_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The starting date and time for the events, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_spot_fleet_request_history_max_results.DescribeSpotFleetRequestHistoryMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
