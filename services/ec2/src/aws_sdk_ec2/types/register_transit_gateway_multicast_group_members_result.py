"""Generated from Smithy shape ``com.amazonaws.ec2#RegisterTransitGatewayMulticastGroupMembersResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_multicast_registered_group_members


class RegisterTransitGatewayMulticastGroupMembersResult(TypedDict):
    registered_multicast_group_members: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_registered_group_members.TransitGatewayMulticastRegisteredGroupMembers"
    ]
    """<p>Information about the registered transit gateway multicast group members.</p>"""
