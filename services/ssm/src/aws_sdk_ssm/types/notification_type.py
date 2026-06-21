"""Generated from Smithy shape ``com.amazonaws.ssm#NotificationType``."""

from typing import Literal, TypeAlias, cast

NotificationType: TypeAlias = Literal[
    "Command",
    "Invocation",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotificationType:
    return cast(NotificationType, data)
