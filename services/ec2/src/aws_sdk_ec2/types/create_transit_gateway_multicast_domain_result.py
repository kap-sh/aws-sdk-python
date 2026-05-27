"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayMulticastDomainResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_multicast_domain


class CreateTransitGatewayMulticastDomainResult(TypedDict):
    transit_gateway_multicast_domain: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_domain.TransitGatewayMulticastDomain"
    ]
    """<p>Information about the transit gateway multicast domain.</p>"""
