"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotState``."""

from typing import Literal, TypeAlias

SnapshotState: TypeAlias = Literal[
    "pending",
    "completed",
    "error",
    "recoverable",
    "recovering",
]
