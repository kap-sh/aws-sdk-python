"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpnConnectionRouteRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpn_connection_id


class CreateVpnConnectionRouteRequest(TypedDict):
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR block associated with the local subnet of the customer network.</p>"""
    vpn_connection_id: NotRequired[
        "aws_sdk_ec2.types.vpn_connection_id.VpnConnectionId"
    ]
    """<p>The ID of the VPN connection.</p>"""
