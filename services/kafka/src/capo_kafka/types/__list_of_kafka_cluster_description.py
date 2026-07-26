"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfKafkaClusterDescription``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafka.types.kafka_cluster_description

__listOfKafkaClusterDescription: TypeAlias = list[
    "capo_kafka.types.kafka_cluster_description.KafkaClusterDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfKafkaClusterDescription) -> list:
    import capo_kafka.types.kafka_cluster_description

    out: list = []
    for item in value:
        out.append(capo_kafka.types.kafka_cluster_description.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfKafkaClusterDescription:
    import capo_kafka.types.kafka_cluster_description

    out: __listOfKafkaClusterDescription = []
    for item in data:
        out.append(capo_kafka.types.kafka_cluster_description.deserialize_json(item))
    return out
