"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClientVpnTargetNetworksResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.target_network_set


class DescribeClientVpnTargetNetworksResult(TypedDict):
    client_vpn_target_networks: NotRequired[
        "aws_sdk_ec2.types.target_network_set.TargetNetworkSet"
    ]
    """<p>Information about the associated target networks.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
