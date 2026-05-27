"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayClientVpnAttachment``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_endpoint_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_attachment_id
    import aws_sdk_ec2.types.transit_gateway_attachment_status_type
    import aws_sdk_ec2.types.transit_gateway_id


class TransitGatewayClientVpnAttachment(TypedDict):
    transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the Transit Gateway attachment.</p>"""
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the Transit Gateway.</p>"""
    client_vpn_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.client_vpn_endpoint_id.ClientVpnEndpointId"
    ]
    """<p>The ID of the Client VPN endpoint.</p>"""
    client_vpn_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the Client VPN endpoint.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_status_type.TransitGatewayAttachmentStatusType"
    ]
    """<p>The state of the Transit Gateway attachment.</p>"""
    creation_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The date and time the Transit Gateway attachment was created.</p>"""
