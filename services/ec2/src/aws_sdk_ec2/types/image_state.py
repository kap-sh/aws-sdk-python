"""Generated from Smithy shape ``com.amazonaws.ec2#ImageState``."""

from typing import Literal, TypeAlias

ImageState: TypeAlias = Literal[
    "pending",
    "available",
    "invalid",
    "deregistered",
    "transient",
    "failed",
    "error",
    "disabled",
]
