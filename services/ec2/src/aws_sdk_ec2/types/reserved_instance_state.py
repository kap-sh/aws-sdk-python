"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstanceState``."""

from typing import Literal, TypeAlias

ReservedInstanceState: TypeAlias = Literal[
    "payment-pending",
    "active",
    "payment-failed",
    "retired",
    "queued",
    "queued-deleted",
]
