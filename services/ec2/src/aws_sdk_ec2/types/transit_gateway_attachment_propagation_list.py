"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachmentPropagationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_attachment_propagation

TransitGatewayAttachmentPropagationList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_attachment_propagation.TransitGatewayAttachmentPropagation"
]
