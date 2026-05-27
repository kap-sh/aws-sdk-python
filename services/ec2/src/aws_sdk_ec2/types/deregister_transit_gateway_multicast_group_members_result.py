"""Generated from Smithy shape ``com.amazonaws.ec2#DeregisterTransitGatewayMulticastGroupMembersResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_multicast_deregistered_group_members


class DeregisterTransitGatewayMulticastGroupMembersResult(TypedDict):
    deregistered_multicast_group_members: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_deregistered_group_members.TransitGatewayMulticastDeregisteredGroupMembers"
    ]
    """<p>Information about the deregistered members.</p>"""
