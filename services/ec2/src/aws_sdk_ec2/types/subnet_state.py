"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetState``."""

from typing import Literal, TypeAlias

SubnetState: TypeAlias = Literal[
    "pending",
    "available",
    "unavailable",
    "failed",
    "failed-insufficient-capacity",
]
