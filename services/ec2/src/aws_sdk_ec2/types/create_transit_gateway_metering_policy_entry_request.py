"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayMeteringPolicyEntryRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_attachment_id
    import aws_sdk_ec2.types.transit_gateway_attachment_resource_type
    import aws_sdk_ec2.types.transit_gateway_metering_payer_type
    import aws_sdk_ec2.types.transit_gateway_metering_policy_id


class CreateTransitGatewayMeteringPolicyEntryRequest(TypedDict):
    transit_gateway_metering_policy_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_metering_policy_id.TransitGatewayMeteringPolicyId"
    ]
    """<p>The ID of the transit gateway metering policy to add the entry to.</p>"""
    policy_rule_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The rule number for the metering policy entry. Rules are processed in order from lowest to highest number.</p>"""
    source_transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the source transit gateway attachment for traffic matching.</p>"""
    source_transit_gateway_attachment_type: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The type of the source transit gateway attachment for traffic matching. Note that the <code>tgw-peering</code> resource type has been deprecated. To configure metering policies for Connect, use the transport attachment type.</p>"""
    source_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source CIDR block for traffic matching.</p>"""
    source_port_range: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source port range for traffic matching.</p>"""
    destination_transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the destination transit gateway attachment for traffic matching.</p>"""
    destination_transit_gateway_attachment_type: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The type of the destination transit gateway attachment for traffic matching. Note that the <code>tgw-peering</code> resource type has been deprecated. To configure metering policies for Connect, use the transport attachment type.</p>"""
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The destination CIDR block for traffic matching.</p>"""
    destination_port_range: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The destination port range for traffic matching.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The protocol for traffic matching (1, 6, 17, etc.).</p>"""
    metered_account: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_metering_payer_type.TransitGatewayMeteringPayerType"
    ]
    """<p>The Amazon Web Services account ID to which the metered traffic should be attributed.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
