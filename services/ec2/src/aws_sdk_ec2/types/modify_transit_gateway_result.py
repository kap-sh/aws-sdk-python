"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTransitGatewayResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway


class ModifyTransitGatewayResult(TypedDict):
    transit_gateway: NotRequired["aws_sdk_ec2.types.transit_gateway.TransitGateway"]
    """<p>Information about the transit gateway.</p>"""
