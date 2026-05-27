"""Generated from Smithy shape ``com.amazonaws.ec2#VpcBlockPublicAccessExclusionState``."""

from typing import Literal, TypeAlias

VpcBlockPublicAccessExclusionState: TypeAlias = Literal[
    "create-in-progress",
    "create-complete",
    "create-failed",
    "update-in-progress",
    "update-complete",
    "update-failed",
    "delete-in-progress",
    "delete-complete",
    "disable-in-progress",
    "disable-complete",
]
