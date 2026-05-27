"""Generated from Smithy shape ``com.amazonaws.ec2#AllocationState``."""

from typing import Literal, TypeAlias

AllocationState: TypeAlias = Literal[
    "available",
    "under-assessment",
    "permanent-failure",
    "released",
    "released-permanent-failure",
    "pending",
]
