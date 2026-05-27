"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpnConcentratorsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.vpn_concentrator_list


class DescribeVpnConcentratorsResult(TypedDict):
    vpn_concentrators: NotRequired[
        "aws_sdk_ec2.types.vpn_concentrator_list.VpnConcentratorList"
    ]
    """<p>Information about the VPN concentrators.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
