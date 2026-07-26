"""Generated from Smithy shape ``com.amazonaws.kafka#ReplicationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.consumer_group_replication
    import capo_kafka.types.target_compression_type
    import capo_kafka.types.topic_replication


class ReplicationInfo(TypedDict, closed=True):
    consumer_group_replication: NotRequired[
        "capo_kafka.types.consumer_group_replication.ConsumerGroupReplication"
    ]
    """<p>Configuration relating to consumer group replication.</p>"""
    source_kafka_cluster_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The ARN of the source Kafka cluster.</p>"""
    source_kafka_cluster_id: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The ID of the source Kafka cluster.</p>"""
    target_compression_type: NotRequired[
        "capo_kafka.types.target_compression_type.TargetCompressionType"
    ]
    """<p>The compression type to use when producing records to target cluster.</p>"""
    target_kafka_cluster_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The ARN of the target Kafka cluster.</p>"""
    target_kafka_cluster_id: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The ID of the target Kafka cluster.</p>"""
    topic_replication: NotRequired[
        "capo_kafka.types.topic_replication.TopicReplication"
    ]
    """<p>Configuration relating to topic replication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationInfo) -> dict:
    out: dict = {}
    if "consumer_group_replication" in value:
        import capo_kafka.types.consumer_group_replication

        out["consumerGroupReplication"] = (
            capo_kafka.types.consumer_group_replication.serialize_json(
                value["consumer_group_replication"]
            )
        )
    if "source_kafka_cluster_arn" in value:
        out["sourceKafkaClusterArn"] = value["source_kafka_cluster_arn"]
    if "source_kafka_cluster_id" in value:
        out["sourceKafkaClusterId"] = value["source_kafka_cluster_id"]
    if "target_compression_type" in value:
        import capo_kafka.types.target_compression_type

        out["targetCompressionType"] = (
            capo_kafka.types.target_compression_type.serialize_json(
                value["target_compression_type"]
            )
        )
    if "target_kafka_cluster_arn" in value:
        out["targetKafkaClusterArn"] = value["target_kafka_cluster_arn"]
    if "target_kafka_cluster_id" in value:
        out["targetKafkaClusterId"] = value["target_kafka_cluster_id"]
    if "topic_replication" in value:
        import capo_kafka.types.topic_replication

        out["topicReplication"] = capo_kafka.types.topic_replication.serialize_json(
            value["topic_replication"]
        )
    return out


def deserialize_json(data: dict) -> ReplicationInfo:
    out: ReplicationInfo = {}  # type: ignore[typeddict-item]
    if "consumerGroupReplication" in data:
        import capo_kafka.types.consumer_group_replication

        out["consumer_group_replication"] = (
            capo_kafka.types.consumer_group_replication.deserialize_json(
                data["consumerGroupReplication"]
            )
        )
    if "sourceKafkaClusterArn" in data:
        out["source_kafka_cluster_arn"] = data["sourceKafkaClusterArn"]
    if "sourceKafkaClusterId" in data:
        out["source_kafka_cluster_id"] = data["sourceKafkaClusterId"]
    if "targetCompressionType" in data:
        import capo_kafka.types.target_compression_type

        out["target_compression_type"] = (
            capo_kafka.types.target_compression_type.deserialize_json(
                data["targetCompressionType"]
            )
        )
    if "targetKafkaClusterArn" in data:
        out["target_kafka_cluster_arn"] = data["targetKafkaClusterArn"]
    if "targetKafkaClusterId" in data:
        out["target_kafka_cluster_id"] = data["targetKafkaClusterId"]
    if "topicReplication" in data:
        import capo_kafka.types.topic_replication

        out["topic_replication"] = capo_kafka.types.topic_replication.deserialize_json(
            data["topicReplication"]
        )
    return out
