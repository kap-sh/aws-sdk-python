"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayVpcAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_vpc_attachment

TransitGatewayVpcAttachmentList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_vpc_attachment.TransitGatewayVpcAttachment"
]
