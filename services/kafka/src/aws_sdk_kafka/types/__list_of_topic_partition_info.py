"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfTopicPartitionInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafka.types.topic_partition_info

__listOfTopicPartitionInfo: TypeAlias = list[
    "aws_sdk_kafka.types.topic_partition_info.TopicPartitionInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfTopicPartitionInfo) -> list:
    import aws_sdk_kafka.types.topic_partition_info

    out: list = []
    for item in value:
        out.append(aws_sdk_kafka.types.topic_partition_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfTopicPartitionInfo:
    import aws_sdk_kafka.types.topic_partition_info

    out: __listOfTopicPartitionInfo = []
    for item in data:
        out.append(aws_sdk_kafka.types.topic_partition_info.deserialize_json(item))
    return out
