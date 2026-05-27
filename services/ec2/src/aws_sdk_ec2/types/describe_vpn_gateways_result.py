"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpnGatewaysResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpn_gateway_list


class DescribeVpnGatewaysResult(TypedDict):
    vpn_gateways: NotRequired["aws_sdk_ec2.types.vpn_gateway_list.VpnGatewayList"]
    """<p>Information about one or more virtual private gateways.</p>"""
