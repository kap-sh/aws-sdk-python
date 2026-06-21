"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ScheduledQueryInsightsMode``."""

from typing import Literal, TypeAlias, cast

ScheduledQueryInsightsMode: TypeAlias = Literal[
    "ENABLED_WITH_RATE_CONTROL",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduledQueryInsightsMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ScheduledQueryInsightsMode:
    return cast(ScheduledQueryInsightsMode, data)
