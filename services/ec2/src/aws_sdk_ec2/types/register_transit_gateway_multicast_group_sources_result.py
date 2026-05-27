"""Generated from Smithy shape ``com.amazonaws.ec2#RegisterTransitGatewayMulticastGroupSourcesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_multicast_registered_group_sources


class RegisterTransitGatewayMulticastGroupSourcesResult(TypedDict):
    registered_multicast_group_sources: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_registered_group_sources.TransitGatewayMulticastRegisteredGroupSources"
    ]
    """<p>Information about the transit gateway multicast group sources.</p>"""
