"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointConnectionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class DescribeVpcEndpointConnectionsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>ip-address-type</code> - The IP address type (<code>ipv4</code> | <code>ipv6</code>).</p> </li> <li> <p> <code>service-id</code> - The ID of the service.</p> </li> <li> <p> <code>vpc-endpoint-owner</code> - The ID of the Amazon Web Services account ID that owns the endpoint.</p> </li> <li> <p> <code>vpc-endpoint-region</code> - The Region of the endpoint or <code>cross-region</code> to find endpoints for other Regions.</p> </li> <li> <p> <code>vpc-endpoint-state</code> - The state of the endpoint (<code>pendingAcceptance</code> | <code>pending</code> | <code>available</code> | <code>deleting</code> | <code>deleted</code> | <code>rejected</code> | <code>failed</code>).</p> </li> <li> <p> <code>vpc-endpoint-id</code> - The ID of the endpoint.</p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of results to return for the request in a single page. The remaining results of the initial request can be seen by sending another request with the returned <code>NextToken</code> value. This value can be between 5 and 1,000; if <code>MaxResults</code> is given a value larger than 1,000, only 1,000 results are returned.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to retrieve the next page of results.</p>"""
