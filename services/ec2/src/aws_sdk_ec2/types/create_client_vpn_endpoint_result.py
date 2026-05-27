"""Generated from Smithy shape ``com.amazonaws.ec2#CreateClientVpnEndpointResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_endpoint_status
    import aws_sdk_ec2.types.string


class CreateClientVpnEndpointResult(TypedDict):
    client_vpn_endpoint_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Client VPN endpoint.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_status.ClientVpnEndpointStatus"
    ]
    """<p>The current state of the Client VPN endpoint.</p>"""
    dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The DNS name to be used by clients when establishing their VPN session.</p>"""
