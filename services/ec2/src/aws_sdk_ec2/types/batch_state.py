"""Generated from Smithy shape ``com.amazonaws.ec2#BatchState``."""

from typing import Literal, TypeAlias

BatchState: TypeAlias = Literal[
    "submitted",
    "active",
    "cancelled",
    "failed",
    "cancelled_running",
    "cancelled_terminating",
    "modifying",
]
