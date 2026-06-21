"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ScheduledQueryRunStatus``."""

from typing import Literal, TypeAlias, cast

ScheduledQueryRunStatus: TypeAlias = Literal[
    "AUTO_TRIGGER_SUCCESS",
    "AUTO_TRIGGER_FAILURE",
    "MANUAL_TRIGGER_SUCCESS",
    "MANUAL_TRIGGER_FAILURE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduledQueryRunStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ScheduledQueryRunStatus:
    return cast(ScheduledQueryRunStatus, data)
