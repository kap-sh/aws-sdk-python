"""Generated from Smithy shape ``com.amazonaws.ecs#TaskStopCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

TaskStopCode: TypeAlias = Literal[
    "TaskFailedToStart",
    "EssentialContainerExited",
    "UserInitiated",
    "ServiceSchedulerInitiated",
    "SpotInterruption",
    "TerminationNotice",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TaskFailedToStart",
        "EssentialContainerExited",
        "UserInitiated",
        "ServiceSchedulerInitiated",
        "SpotInterruption",
        "TerminationNotice",
    )
)


def serialize_aws_json_1_1(value: TaskStopCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskStopCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskStopCode value: {data!r}")
    return cast(TaskStopCode, data)
