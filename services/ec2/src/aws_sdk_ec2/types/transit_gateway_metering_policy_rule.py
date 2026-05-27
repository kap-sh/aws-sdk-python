"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMeteringPolicyRule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_attachment_id
    import aws_sdk_ec2.types.transit_gateway_attachment_resource_type


class TransitGatewayMeteringPolicyRule(TypedDict):
    source_transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the source transit gateway attachment.</p>"""
    source_transit_gateway_attachment_type: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The type of the source transit gateway attachment. Note that the <code>tgw-peering</code> resource type has been deprecated. To configure metering policies for Connect, use the transport attachment type.</p>"""
    source_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source CIDR block for the rule.</p>"""
    source_port_range: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source port range for the rule.</p>"""
    destination_transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the destination transit gateway attachment.</p>"""
    destination_transit_gateway_attachment_type: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The type of the destination transit gateway attachment. Note that the <code>tgw-peering</code> resource type has been deprecated. To configure metering policies for Connect, use the transport attachment type.</p>"""
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The destination CIDR block for the rule.</p>"""
    destination_port_range: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The destination port range for the rule.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The protocol for the rule (1, 6, 17, etc.).</p>"""
