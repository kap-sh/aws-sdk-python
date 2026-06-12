"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfKafkaClusterDescription``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafka.types.kafka_cluster_description

__listOfKafkaClusterDescription: TypeAlias = list[
    "aws_sdk_kafka.types.kafka_cluster_description.KafkaClusterDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfKafkaClusterDescription) -> list:
    import aws_sdk_kafka.types.kafka_cluster_description

    out: list = []
    for item in value:
        out.append(aws_sdk_kafka.types.kafka_cluster_description.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfKafkaClusterDescription:
    import aws_sdk_kafka.types.kafka_cluster_description

    out: __listOfKafkaClusterDescription = []
    for item in data:
        out.append(aws_sdk_kafka.types.kafka_cluster_description.deserialize_json(item))
    return out
