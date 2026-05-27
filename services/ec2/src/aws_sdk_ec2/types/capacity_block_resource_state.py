"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockResourceState``."""

from typing import Literal, TypeAlias

CapacityBlockResourceState: TypeAlias = Literal[
    "active",
    "expired",
    "unavailable",
    "cancelled",
    "failed",
    "scheduled",
    "payment-pending",
    "payment-failed",
]
