"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachmentIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_attachment_id

TransitGatewayAttachmentIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
]
