"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfKafkaClusterSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafka.types.kafka_cluster_summary

__listOfKafkaClusterSummary: TypeAlias = list[
    "aws_sdk_kafka.types.kafka_cluster_summary.KafkaClusterSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfKafkaClusterSummary) -> list:
    import aws_sdk_kafka.types.kafka_cluster_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_kafka.types.kafka_cluster_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfKafkaClusterSummary:
    import aws_sdk_kafka.types.kafka_cluster_summary

    out: __listOfKafkaClusterSummary = []
    for item in data:
        out.append(aws_sdk_kafka.types.kafka_cluster_summary.deserialize_json(item))
    return out
