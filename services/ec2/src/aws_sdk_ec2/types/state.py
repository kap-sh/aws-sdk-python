"""Generated from Smithy shape ``com.amazonaws.ec2#State``."""

from typing import Literal, TypeAlias

State: TypeAlias = Literal[
    "PendingAcceptance",
    "Pending",
    "Available",
    "Deleting",
    "Deleted",
    "Rejected",
    "Failed",
    "Expired",
    "Partial",
]
