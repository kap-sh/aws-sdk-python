"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationState``."""

from typing import Literal, TypeAlias

CapacityReservationState: TypeAlias = Literal[
    "active",
    "expired",
    "cancelled",
    "pending",
    "failed",
    "scheduled",
    "payment-pending",
    "payment-failed",
    "assessing",
    "delayed",
    "unsupported",
    "unavailable",
]
