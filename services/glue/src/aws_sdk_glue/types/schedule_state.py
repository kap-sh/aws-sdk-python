"""Generated from Smithy shape ``com.amazonaws.glue#ScheduleState``."""

from typing import Literal, TypeAlias, cast

ScheduleState: TypeAlias = Literal[
    "SCHEDULED",
    "NOT_SCHEDULED",
    "TRANSITIONING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduleState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScheduleState:
    return cast(ScheduleState, data)
