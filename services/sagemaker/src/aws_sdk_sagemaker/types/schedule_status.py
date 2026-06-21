"""Generated from Smithy shape ``com.amazonaws.sagemaker#ScheduleStatus``."""

from typing import Literal, TypeAlias, cast

ScheduleStatus: TypeAlias = Literal[
    "Pending",
    "Failed",
    "Scheduled",
    "Stopped",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduleStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScheduleStatus:
    return cast(ScheduleStatus, data)
