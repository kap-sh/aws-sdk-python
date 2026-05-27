"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastGroup``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.membership_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_attachment_resource_type


class TransitGatewayMulticastGroup(TypedDict):
    group_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IP address assigned to the transit gateway multicast group.</p>"""
    transit_gateway_attachment_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway attachment.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The type of resource, for example a VPC attachment.</p>"""
    resource_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The ID of the Amazon Web Services account that owns the transit gateway multicast domain group resource.</p>"""
    network_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway attachment.</p>"""
    group_member: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates that the resource is a transit gateway multicast group member.</p>"""
    group_source: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates that the resource is a transit gateway multicast group member.</p>"""
    member_type: NotRequired["aws_sdk_ec2.types.membership_type.MembershipType"]
    """<p>The member type (for example, <code>static</code>).</p>"""
    source_type: NotRequired["aws_sdk_ec2.types.membership_type.MembershipType"]
    """<p>The source type.</p>"""
