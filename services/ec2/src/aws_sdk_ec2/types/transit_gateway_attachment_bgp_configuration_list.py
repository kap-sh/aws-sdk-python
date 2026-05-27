"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachmentBgpConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_attachment_bgp_configuration

TransitGatewayAttachmentBgpConfigurationList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_attachment_bgp_configuration.TransitGatewayAttachmentBgpConfiguration"
]
