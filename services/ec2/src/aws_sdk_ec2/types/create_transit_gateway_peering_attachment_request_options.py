"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayPeeringAttachmentRequestOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dynamic_routing_value


class CreateTransitGatewayPeeringAttachmentRequestOptions(TypedDict):
    dynamic_routing: NotRequired[
        "aws_sdk_ec2.types.dynamic_routing_value.DynamicRoutingValue"
    ]
    """<p>Indicates whether dynamic routing is enabled or disabled.</p>"""
