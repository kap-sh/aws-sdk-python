"""Generated from Smithy shape ``com.amazonaws.ssm#NotificationEvent``."""

from typing import Literal, TypeAlias, cast

NotificationEvent: TypeAlias = Literal[
    "All",
    "InProgress",
    "Success",
    "TimedOut",
    "Cancelled",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationEvent) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotificationEvent:
    return cast(NotificationEvent, data)
