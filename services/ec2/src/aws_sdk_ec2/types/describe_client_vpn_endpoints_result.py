"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClientVpnEndpointsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.endpoint_set
    import aws_sdk_ec2.types.next_token


class DescribeClientVpnEndpointsResult(TypedDict):
    client_vpn_endpoints: NotRequired["aws_sdk_ec2.types.endpoint_set.EndpointSet"]
    """<p>Information about the Client VPN endpoints.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
