"""Generated from Smithy shape ``com.amazonaws.timestreamquery#QueryInsightsMode``."""

from typing import Literal, TypeAlias, cast

QueryInsightsMode: TypeAlias = Literal[
    "ENABLED_WITH_RATE_CONTROL",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueryInsightsMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> QueryInsightsMode:
    return cast(QueryInsightsMode, data)
