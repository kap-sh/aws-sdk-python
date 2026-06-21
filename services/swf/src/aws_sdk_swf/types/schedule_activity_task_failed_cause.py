"""Generated from Smithy shape ``com.amazonaws.swf#ScheduleActivityTaskFailedCause``."""

from typing import Literal, TypeAlias, cast

ScheduleActivityTaskFailedCause: TypeAlias = Literal[
    "ACTIVITY_TYPE_DEPRECATED",
    "ACTIVITY_TYPE_DOES_NOT_EXIST",
    "ACTIVITY_ID_ALREADY_IN_USE",
    "OPEN_ACTIVITIES_LIMIT_EXCEEDED",
    "ACTIVITY_CREATION_RATE_EXCEEDED",
    "DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED",
    "DEFAULT_TASK_LIST_UNDEFINED",
    "DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED",
    "DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED",
    "OPERATION_NOT_PERMITTED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduleActivityTaskFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ScheduleActivityTaskFailedCause:
    return cast(ScheduleActivityTaskFailedCause, data)
