"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClientVpnConnectionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_connection_set
    import aws_sdk_ec2.types.next_token


class DescribeClientVpnConnectionsResult(TypedDict):
    connections: NotRequired[
        "aws_sdk_ec2.types.client_vpn_connection_set.ClientVpnConnectionSet"
    ]
    """<p>Information about the active and terminated client connections.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
