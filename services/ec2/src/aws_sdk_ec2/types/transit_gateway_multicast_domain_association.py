"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastDomainAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_association
    import aws_sdk_ec2.types.transit_gateway_attachment_resource_type


class TransitGatewayMulticastDomainAssociation(TypedDict):
    transit_gateway_attachment_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway attachment.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The type of resource, for example a VPC attachment.</p>"""
    resource_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The ID of the Amazon Web Services account that owns the transit gateway multicast domain association resource.</p>"""
    subnet: NotRequired["aws_sdk_ec2.types.subnet_association.SubnetAssociation"]
    """<p>The subnet associated with the transit gateway multicast domain.</p>"""
