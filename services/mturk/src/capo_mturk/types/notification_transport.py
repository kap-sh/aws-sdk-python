"""Generated from Smithy shape ``com.amazonaws.mturk#NotificationTransport``."""

from typing import Literal, TypeAlias, cast

NotificationTransport: TypeAlias = Literal[
    "Email",
    "SQS",
    "SNS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationTransport) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotificationTransport:
    return cast(NotificationTransport, data)
