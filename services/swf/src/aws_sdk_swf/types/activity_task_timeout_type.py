"""Generated from Smithy shape ``com.amazonaws.swf#ActivityTaskTimeoutType``."""

from typing import Literal, TypeAlias, cast

ActivityTaskTimeoutType: TypeAlias = Literal[
    "START_TO_CLOSE",
    "SCHEDULE_TO_START",
    "SCHEDULE_TO_CLOSE",
    "HEARTBEAT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityTaskTimeoutType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ActivityTaskTimeoutType:
    return cast(ActivityTaskTimeoutType, data)
