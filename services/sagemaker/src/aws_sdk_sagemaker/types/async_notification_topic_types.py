"""Generated from Smithy shape ``com.amazonaws.sagemaker#AsyncNotificationTopicTypes``."""

from typing import Literal, TypeAlias, cast

AsyncNotificationTopicTypes: TypeAlias = Literal[
    "SUCCESS_NOTIFICATION_TOPIC",
    "ERROR_NOTIFICATION_TOPIC",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AsyncNotificationTopicTypes) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AsyncNotificationTopicTypes:
    return cast(AsyncNotificationTopicTypes, data)
