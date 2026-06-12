"""Generated from Smithy shape ``com.amazonaws.sagemaker#AsyncNotificationTopicTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.async_notification_topic_types

AsyncNotificationTopicTypeList: TypeAlias = list[
    "aws_sdk_sagemaker.types.async_notification_topic_types.AsyncNotificationTopicTypes"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AsyncNotificationTopicTypeList) -> list:
    import aws_sdk_sagemaker.types.async_notification_topic_types

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.async_notification_topic_types.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AsyncNotificationTopicTypeList:
    import aws_sdk_sagemaker.types.async_notification_topic_types

    out: AsyncNotificationTopicTypeList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.async_notification_topic_types.deserialize_aws_json_1_1(
                item
            )
        )
    return out
