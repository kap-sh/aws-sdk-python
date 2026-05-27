"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerEndpointState``."""

from typing import Literal, TypeAlias

RouteServerEndpointState: TypeAlias = Literal[
    "pending",
    "available",
    "deleting",
    "deleted",
    "failing",
    "failed",
    "delete-failed",
]
