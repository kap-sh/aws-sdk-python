"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceEventWindowsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.instance_event_window_id_set
    import aws_sdk_ec2.types.result_range
    import aws_sdk_ec2.types.string


class DescribeInstanceEventWindowsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_event_window_ids: NotRequired[
        "aws_sdk_ec2.types.instance_event_window_id_set.InstanceEventWindowIdSet"
    ]
    """<p>The IDs of the event windows.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>dedicated-host-id</code> - The event windows associated with the specified Dedicated Host ID.</p> </li> <li> <p> <code>event-window-name</code> - The event windows associated with the specified names. </p> </li> <li> <p> <code>instance-id</code> - The event windows associated with the specified instance ID.</p> </li> <li> <p> <code>instance-tag</code> - The event windows associated with the specified tag and value.</p> </li> <li> <p> <code>instance-tag-key</code> - The event windows associated with the specified tag key, regardless of the value.</p> </li> <li> <p> <code>instance-tag-value</code> - The event windows associated with the specified tag value, regardless of the key.</p> </li> <li> <p> <code>tag:<key></code> - The key/value combination of a tag assigned to the event window. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>CMX</code>, specify <code>tag:Owner</code> for the filter name and <code>CMX</code> for the filter value. </p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the event window. Use this filter to find all event windows that have a tag with a specific key, regardless of the tag value. </p> </li> <li> <p> <code>tag-value</code> - The value of a tag assigned to the event window. Use this filter to find all event windows that have a tag with a specific value, regardless of the tag key. </p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_ec2.types.result_range.ResultRange"]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value. This value can be between 20 and 500. You cannot specify this parameter and the event window IDs parameter in the same call.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to request the next page of results.</p>"""
