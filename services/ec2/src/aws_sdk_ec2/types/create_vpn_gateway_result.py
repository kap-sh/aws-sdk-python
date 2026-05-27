"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpnGatewayResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpn_gateway


class CreateVpnGatewayResult(TypedDict):
    vpn_gateway: NotRequired["aws_sdk_ec2.types.vpn_gateway.VpnGateway"]
    """<p>Information about the virtual private gateway.</p>"""
