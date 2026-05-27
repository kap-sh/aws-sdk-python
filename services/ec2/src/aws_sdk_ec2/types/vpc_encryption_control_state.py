"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionControlState``."""

from typing import Literal, TypeAlias

VpcEncryptionControlState: TypeAlias = Literal[
    "enforce-in-progress",
    "monitor-in-progress",
    "enforce-failed",
    "monitor-failed",
    "deleting",
    "deleted",
    "available",
    "creating",
    "delete-failed",
]
