"""Generated from Smithy shape ``com.amazonaws.ec2#VpcPeeringConnectionStateReasonCode``."""

from typing import Literal, TypeAlias

VpcPeeringConnectionStateReasonCode: TypeAlias = Literal[
    "initiating-request",
    "pending-acceptance",
    "active",
    "deleted",
    "rejected",
    "failed",
    "expired",
    "provisioning",
    "deleting",
]
