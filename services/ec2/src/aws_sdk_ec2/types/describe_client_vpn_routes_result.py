"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClientVpnRoutesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_route_set
    import aws_sdk_ec2.types.next_token


class DescribeClientVpnRoutesResult(TypedDict):
    routes: NotRequired["aws_sdk_ec2.types.client_vpn_route_set.ClientVpnRouteSet"]
    """<p>Information about the Client VPN endpoint routes.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
