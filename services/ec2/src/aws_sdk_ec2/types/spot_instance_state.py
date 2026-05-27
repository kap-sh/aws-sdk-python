"""Generated from Smithy shape ``com.amazonaws.ec2#SpotInstanceState``."""

from typing import Literal, TypeAlias

SpotInstanceState: TypeAlias = Literal[
    "open",
    "active",
    "closed",
    "cancelled",
    "failed",
    "disabled",
]
