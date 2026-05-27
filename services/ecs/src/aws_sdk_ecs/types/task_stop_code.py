"""Generated from Smithy shape ``com.amazonaws.ecs#TaskStopCode``."""

from typing import Literal, TypeAlias

TaskStopCode: TypeAlias = Literal[
    "TaskFailedToStart",
    "EssentialContainerExited",
    "UserInitiated",
    "ServiceSchedulerInitiated",
    "SpotInterruption",
    "TerminationNotice",
]
