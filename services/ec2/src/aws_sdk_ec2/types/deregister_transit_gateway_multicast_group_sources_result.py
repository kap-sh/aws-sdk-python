"""Generated from Smithy shape ``com.amazonaws.ec2#DeregisterTransitGatewayMulticastGroupSourcesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_multicast_deregistered_group_sources


class DeregisterTransitGatewayMulticastGroupSourcesResult(TypedDict):
    deregistered_multicast_group_sources: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_deregistered_group_sources.TransitGatewayMulticastDeregisteredGroupSources"
    ]
    """<p>Information about the deregistered group sources.</p>"""
