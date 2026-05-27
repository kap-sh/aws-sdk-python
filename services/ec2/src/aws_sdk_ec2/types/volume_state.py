"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeState``."""

from typing import Literal, TypeAlias

VolumeState: TypeAlias = Literal[
    "creating",
    "available",
    "in-use",
    "deleting",
    "deleted",
    "error",
]
