"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteTableAnnouncementState``."""

from typing import Literal, TypeAlias

TransitGatewayRouteTableAnnouncementState: TypeAlias = Literal[
    "available",
    "pending",
    "failing",
    "failed",
    "deleting",
    "deleted",
]
