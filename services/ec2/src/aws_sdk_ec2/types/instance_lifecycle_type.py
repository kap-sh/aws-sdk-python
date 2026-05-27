"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceLifecycleType``."""

from typing import Literal, TypeAlias

InstanceLifecycleType: TypeAlias = Literal[
    "spot",
    "scheduled",
    "capacity-block",
    "interruptible-capacity-reservation",
]
