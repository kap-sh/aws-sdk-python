"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachmentStatusType``."""

from typing import Literal, TypeAlias

TransitGatewayAttachmentStatusType: TypeAlias = Literal[
    "pending-acceptance",
    "pending",
    "rejected",
    "available",
    "deleting",
    "deleted",
]
