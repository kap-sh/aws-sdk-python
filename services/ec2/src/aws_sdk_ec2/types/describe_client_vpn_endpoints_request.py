"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClientVpnEndpointsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.client_vpn_endpoint_id_list
    import aws_sdk_ec2.types.describe_client_vpn_endpoint_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.next_token


class DescribeClientVpnEndpointsRequest(TypedDict):
    client_vpn_endpoint_ids: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_id_list.ClientVpnEndpointIdList"
    ]
    """<p>The ID of the Client VPN endpoint.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_client_vpn_endpoint_max_results.DescribeClientVpnEndpointMaxResults"
    ]
    """<p>The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the nextToken value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to retrieve the next page of results.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. Filter names and values are case-sensitive.</p> <ul> <li> <p> <code>endpoint-id</code> - The ID of the Client VPN endpoint.</p> </li> <li> <p> <code>transport-protocol</code> - The transport protocol (<code>tcp</code> | <code>udp</code>).</p> </li> </ul>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
