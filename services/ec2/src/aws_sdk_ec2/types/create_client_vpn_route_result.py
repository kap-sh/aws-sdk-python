"""Generated from Smithy shape ``com.amazonaws.ec2#CreateClientVpnRouteResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_route_status


class CreateClientVpnRouteResult(TypedDict):
    status: NotRequired[
        "aws_sdk_ec2.types.client_vpn_route_status.ClientVpnRouteStatus"
    ]
    """<p>The current state of the route.</p>"""
