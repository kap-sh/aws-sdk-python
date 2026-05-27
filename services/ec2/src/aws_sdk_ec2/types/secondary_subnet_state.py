"""Generated from Smithy shape ``com.amazonaws.ec2#SecondarySubnetState``."""

from typing import Literal, TypeAlias

SecondarySubnetState: TypeAlias = Literal[
    "create-in-progress",
    "create-complete",
    "create-failed",
    "delete-in-progress",
    "delete-complete",
    "delete-failed",
]
