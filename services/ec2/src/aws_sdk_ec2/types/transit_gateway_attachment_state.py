"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachmentState``."""

from typing import Literal, TypeAlias

TransitGatewayAttachmentState: TypeAlias = Literal[
    "initiating",
    "initiatingRequest",
    "pendingAcceptance",
    "rollingBack",
    "pending",
    "available",
    "modifying",
    "deleting",
    "deleted",
    "failed",
    "rejected",
    "rejecting",
    "failing",
]
