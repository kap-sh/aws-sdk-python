"""Generated from Smithy shape ``com.amazonaws.kafka#ReplicationInfoDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.consumer_group_replication
    import aws_sdk_kafka.types.target_compression_type
    import aws_sdk_kafka.types.topic_replication


class ReplicationInfoDescription(TypedDict):
    consumer_group_replication: NotRequired[
        "aws_sdk_kafka.types.consumer_group_replication.ConsumerGroupReplication"
    ]
    """<p>Configuration relating to consumer group replication.</p>"""
    source_kafka_cluster_alias: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The alias of the source Kafka cluster.</p>"""
    target_compression_type: NotRequired[
        "aws_sdk_kafka.types.target_compression_type.TargetCompressionType"
    ]
    """<p>The compression type to use when producing records to target cluster.</p>"""
    target_kafka_cluster_alias: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The alias of the target Kafka cluster.</p>"""
    topic_replication: NotRequired[
        "aws_sdk_kafka.types.topic_replication.TopicReplication"
    ]
    """<p>Configuration relating to topic replication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationInfoDescription) -> dict:
    out: dict = {}
    if "consumer_group_replication" in value:
        import aws_sdk_kafka.types.consumer_group_replication

        out["consumerGroupReplication"] = (
            aws_sdk_kafka.types.consumer_group_replication.serialize_json(
                value["consumer_group_replication"]
            )
        )
    if "source_kafka_cluster_alias" in value:
        out["sourceKafkaClusterAlias"] = value["source_kafka_cluster_alias"]
    if "target_compression_type" in value:
        import aws_sdk_kafka.types.target_compression_type

        out["targetCompressionType"] = (
            aws_sdk_kafka.types.target_compression_type.serialize_json(
                value["target_compression_type"]
            )
        )
    if "target_kafka_cluster_alias" in value:
        out["targetKafkaClusterAlias"] = value["target_kafka_cluster_alias"]
    if "topic_replication" in value:
        import aws_sdk_kafka.types.topic_replication

        out["topicReplication"] = aws_sdk_kafka.types.topic_replication.serialize_json(
            value["topic_replication"]
        )
    return out


def deserialize_json(data: dict) -> ReplicationInfoDescription:
    out: ReplicationInfoDescription = {}  # type: ignore[typeddict-item]
    if "consumerGroupReplication" in data:
        import aws_sdk_kafka.types.consumer_group_replication

        out["consumer_group_replication"] = (
            aws_sdk_kafka.types.consumer_group_replication.deserialize_json(
                data["consumerGroupReplication"]
            )
        )
    if "sourceKafkaClusterAlias" in data:
        out["source_kafka_cluster_alias"] = data["sourceKafkaClusterAlias"]
    if "targetCompressionType" in data:
        import aws_sdk_kafka.types.target_compression_type

        out["target_compression_type"] = (
            aws_sdk_kafka.types.target_compression_type.deserialize_json(
                data["targetCompressionType"]
            )
        )
    if "targetKafkaClusterAlias" in data:
        out["target_kafka_cluster_alias"] = data["targetKafkaClusterAlias"]
    if "topicReplication" in data:
        import aws_sdk_kafka.types.topic_replication

        out["topic_replication"] = (
            aws_sdk_kafka.types.topic_replication.deserialize_json(
                data["topicReplication"]
            )
        )
    return out
