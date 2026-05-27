"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnRoute``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_route_status
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_attachment_id


class ClientVpnRoute(TypedDict):
    client_vpn_endpoint_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Client VPN endpoint with which the route is associated.</p>"""
    destination_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address range, in CIDR notation, of the route destination.</p>"""
    target_subnet: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet through which traffic is routed.</p>"""
    type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The route type.</p>"""
    origin: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Indicates how the route was associated with the Client VPN endpoint. <code>associate</code> indicates that the route was automatically added when the target network was associated with the Client VPN endpoint. <code>add-route</code> indicates that the route was manually added using the <b>CreateClientVpnRoute</b> action.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.client_vpn_route_status.ClientVpnRouteStatus"
    ]
    """<p>The current state of the route.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A brief description of the route.</p>"""
    transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the Transit Gateway attachment, if the route targets a Transit Gateway.</p>"""
