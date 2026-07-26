"""Generated from Smithy shape ``com.amazonaws.glue#ScheduleType``."""

from typing import Literal, TypeAlias, cast

ScheduleType: TypeAlias = Literal[
    "CRON",
    "AUTO",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduleType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScheduleType:
    return cast(ScheduleType, data)
