"""Generated from Smithy shape ``com.amazonaws.dynamodb#TimeToLiveStatus``."""

from typing import Literal, TypeAlias, cast

TimeToLiveStatus: TypeAlias = Literal[
    "ENABLING",
    "DISABLING",
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimeToLiveStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TimeToLiveStatus:
    return cast(TimeToLiveStatus, data)
