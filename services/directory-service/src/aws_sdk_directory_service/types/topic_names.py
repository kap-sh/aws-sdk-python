"""Generated from Smithy shape ``com.amazonaws.directoryservice#TopicNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.topic_name

TopicNames: TypeAlias = list["aws_sdk_directory_service.types.topic_name.TopicName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TopicNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TopicNames:
    return list(data)
