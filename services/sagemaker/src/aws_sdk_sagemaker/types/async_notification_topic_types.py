"""Generated from Smithy shape ``com.amazonaws.sagemaker#AsyncNotificationTopicTypes``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AsyncNotificationTopicTypes: TypeAlias = Literal[
    "SUCCESS_NOTIFICATION_TOPIC",
    "ERROR_NOTIFICATION_TOPIC",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS_NOTIFICATION_TOPIC",
        "ERROR_NOTIFICATION_TOPIC",
    )
)


def serialize_aws_json_1_1(value: AsyncNotificationTopicTypes) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AsyncNotificationTopicTypes:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AsyncNotificationTopicTypes value: {data!r}"
        )
    return cast(AsyncNotificationTopicTypes, data)
