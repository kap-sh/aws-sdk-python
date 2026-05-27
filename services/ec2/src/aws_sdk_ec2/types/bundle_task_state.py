"""Generated from Smithy shape ``com.amazonaws.ec2#BundleTaskState``."""

from typing import Literal, TypeAlias

BundleTaskState: TypeAlias = Literal[
    "pending",
    "waiting-for-shutdown",
    "bundling",
    "storing",
    "cancelling",
    "complete",
    "failed",
]
