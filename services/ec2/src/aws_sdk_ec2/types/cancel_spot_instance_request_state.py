"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotInstanceRequestState``."""

from typing import Literal, TypeAlias

CancelSpotInstanceRequestState: TypeAlias = Literal[
    "active",
    "open",
    "closed",
    "cancelled",
    "completed",
]
