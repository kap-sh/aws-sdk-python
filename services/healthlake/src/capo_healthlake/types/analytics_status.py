"""Generated from Smithy shape ``com.amazonaws.healthlake#AnalyticsStatus``."""

from typing import Literal, TypeAlias, cast

AnalyticsStatus: TypeAlias = Literal[
    "ENABLED",
    "ENABLING",
    "DISABLED",
    "DISABLING",
    "PAUSING",
    "PAUSED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AnalyticsStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AnalyticsStatus:
    return cast(AnalyticsStatus, data)
