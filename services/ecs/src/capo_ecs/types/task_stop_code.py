"""Generated from Smithy shape ``com.amazonaws.ecs#TaskStopCode``."""

from typing import Literal, TypeAlias, cast

TaskStopCode: TypeAlias = Literal[
    "TaskFailedToStart",
    "EssentialContainerExited",
    "UserInitiated",
    "ServiceSchedulerInitiated",
    "SpotInterruption",
    "TerminationNotice",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskStopCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskStopCode:
    return cast(TaskStopCode, data)
