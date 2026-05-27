"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerPeerState``."""

from typing import Literal, TypeAlias

RouteServerPeerState: TypeAlias = Literal[
    "pending",
    "available",
    "deleting",
    "deleted",
    "failing",
    "failed",
]
