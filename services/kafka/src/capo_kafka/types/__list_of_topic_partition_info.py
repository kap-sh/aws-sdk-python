"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfTopicPartitionInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafka.types.topic_partition_info

__listOfTopicPartitionInfo: TypeAlias = list[
    "capo_kafka.types.topic_partition_info.TopicPartitionInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfTopicPartitionInfo) -> list:
    import capo_kafka.types.topic_partition_info

    out: list = []
    for item in value:
        out.append(capo_kafka.types.topic_partition_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfTopicPartitionInfo:
    import capo_kafka.types.topic_partition_info

    out: __listOfTopicPartitionInfo = []
    for item in data:
        out.append(capo_kafka.types.topic_partition_info.deserialize_json(item))
    return out
