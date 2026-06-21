"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#ScheduleState``."""

from typing import Literal, TypeAlias, cast

ScheduleState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduleState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ScheduleState:
    return cast(ScheduleState, data)
