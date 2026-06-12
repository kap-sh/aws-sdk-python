"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfKafkaCluster``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafka.types.kafka_cluster

__listOfKafkaCluster: TypeAlias = list["aws_sdk_kafka.types.kafka_cluster.KafkaCluster"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfKafkaCluster) -> list:
    import aws_sdk_kafka.types.kafka_cluster

    out: list = []
    for item in value:
        out.append(aws_sdk_kafka.types.kafka_cluster.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfKafkaCluster:
    import aws_sdk_kafka.types.kafka_cluster

    out: __listOfKafkaCluster = []
    for item in data:
        out.append(aws_sdk_kafka.types.kafka_cluster.deserialize_json(item))
    return out
