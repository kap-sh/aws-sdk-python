"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityManagerMonitoredTagKeysRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.get_capacity_manager_monitored_tag_keys_request_max_results
    import aws_sdk_ec2.types.string


class GetCapacityManagerMonitoredTagKeysRequest(TypedDict):
    max_results: NotRequired[
        "aws_sdk_ec2.types.get_capacity_manager_monitored_tag_keys_request_max_results.GetCapacityManagerMonitoredTagKeysRequestMaxResults"
    ]
    """<p> The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value. If not specified, up to 1000 results are returned. </p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The token for the next page of results. Use the value returned from a previous call to retrieve additional results. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>. </p>"""
