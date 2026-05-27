"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnRouteStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_route_status_code
    import aws_sdk_ec2.types.string


class ClientVpnRouteStatus(TypedDict):
    code: NotRequired[
        "aws_sdk_ec2.types.client_vpn_route_status_code.ClientVpnRouteStatusCode"
    ]
    """<p>The state of the Client VPN endpoint route.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message about the status of the Client VPN endpoint route, if applicable.</p>"""
