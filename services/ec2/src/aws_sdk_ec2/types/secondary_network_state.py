"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryNetworkState``."""

from typing import Literal, TypeAlias

SecondaryNetworkState: TypeAlias = Literal[
    "create-in-progress",
    "create-complete",
    "create-failed",
    "delete-in-progress",
    "delete-complete",
    "delete-failed",
]
