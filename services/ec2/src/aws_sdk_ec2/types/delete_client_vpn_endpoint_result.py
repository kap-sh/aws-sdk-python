"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteClientVpnEndpointResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_endpoint_status


class DeleteClientVpnEndpointResult(TypedDict):
    status: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_status.ClientVpnEndpointStatus"
    ]
    """<p>The current state of the Client VPN endpoint.</p>"""
