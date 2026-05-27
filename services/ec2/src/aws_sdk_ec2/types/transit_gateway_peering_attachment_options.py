"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPeeringAttachmentOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dynamic_routing_value


class TransitGatewayPeeringAttachmentOptions(TypedDict):
    dynamic_routing: NotRequired[
        "aws_sdk_ec2.types.dynamic_routing_value.DynamicRoutingValue"
    ]
    """<p>Describes whether dynamic routing is enabled or disabled for the transit gateway peering attachment.</p>"""
