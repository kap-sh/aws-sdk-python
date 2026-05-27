"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceRootVolumeTaskState``."""

from typing import Literal, TypeAlias

ReplaceRootVolumeTaskState: TypeAlias = Literal[
    "pending",
    "in-progress",
    "failing",
    "succeeded",
    "failed",
    "failed-detached",
]
