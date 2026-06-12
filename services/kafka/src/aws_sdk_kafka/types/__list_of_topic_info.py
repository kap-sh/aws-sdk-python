"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfTopicInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafka.types.topic_info

__listOfTopicInfo: TypeAlias = list["aws_sdk_kafka.types.topic_info.TopicInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfTopicInfo) -> list:
    import aws_sdk_kafka.types.topic_info

    out: list = []
    for item in value:
        out.append(aws_sdk_kafka.types.topic_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfTopicInfo:
    import aws_sdk_kafka.types.topic_info

    out: __listOfTopicInfo = []
    for item in data:
        out.append(aws_sdk_kafka.types.topic_info.deserialize_json(item))
    return out
