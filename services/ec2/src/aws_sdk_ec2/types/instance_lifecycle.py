"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceLifecycle``."""

from typing import Literal, TypeAlias

InstanceLifecycle: TypeAlias = Literal[
    "spot",
    "on-demand",
    "interruptible-capacity-reservation",
]
