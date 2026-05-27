"""Generated from Smithy shape ``com.amazonaws.ec2#ReservationState``."""

from typing import Literal, TypeAlias

ReservationState: TypeAlias = Literal[
    "active",
    "expired",
    "cancelled",
    "scheduled",
    "pending",
    "failed",
    "delayed",
    "unsupported",
    "payment-pending",
    "payment-failed",
    "retired",
]
