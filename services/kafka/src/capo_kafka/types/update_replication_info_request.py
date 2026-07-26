"""Generated from Smithy shape ``com.amazonaws.kafka#UpdateReplicationInfoRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.consumer_group_replication_update
    import capo_kafka.types.log_delivery
    import capo_kafka.types.topic_replication_update


class UpdateReplicationInfoRequest(TypedDict, closed=True):
    consumer_group_replication: NotRequired[
        "capo_kafka.types.consumer_group_replication_update.ConsumerGroupReplicationUpdate"
    ]
    """<p>Updated consumer group replication information.</p>"""
    current_version: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Current replicator version.</p>"""
    replicator_arn: "capo_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the replicator to be updated.</p>"""
    source_kafka_cluster_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The ARN of the source Kafka cluster.</p>"""
    source_kafka_cluster_id: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The ID of the source Kafka cluster.</p>"""
    target_kafka_cluster_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The ARN of the target Kafka cluster.</p>"""
    target_kafka_cluster_id: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The ID of the target Kafka cluster.</p>"""
    topic_replication: NotRequired[
        "capo_kafka.types.topic_replication_update.TopicReplicationUpdate"
    ]
    """<p>Updated topic replication information.</p>"""
    log_delivery: NotRequired["capo_kafka.types.log_delivery.LogDelivery"]
    """<p>Configuration for delivering replicator logs to customer destinations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReplicationInfoRequest) -> dict:
    out: dict = {}
    if "consumer_group_replication" in value:
        import capo_kafka.types.consumer_group_replication_update

        out["consumerGroupReplication"] = (
            capo_kafka.types.consumer_group_replication_update.serialize_json(
                value["consumer_group_replication"]
            )
        )
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "source_kafka_cluster_arn" in value:
        out["sourceKafkaClusterArn"] = value["source_kafka_cluster_arn"]
    if "source_kafka_cluster_id" in value:
        out["sourceKafkaClusterId"] = value["source_kafka_cluster_id"]
    if "target_kafka_cluster_arn" in value:
        out["targetKafkaClusterArn"] = value["target_kafka_cluster_arn"]
    if "target_kafka_cluster_id" in value:
        out["targetKafkaClusterId"] = value["target_kafka_cluster_id"]
    if "topic_replication" in value:
        import capo_kafka.types.topic_replication_update

        out["topicReplication"] = (
            capo_kafka.types.topic_replication_update.serialize_json(
                value["topic_replication"]
            )
        )
    if "log_delivery" in value:
        import capo_kafka.types.log_delivery

        out["logDelivery"] = capo_kafka.types.log_delivery.serialize_json(
            value["log_delivery"]
        )
    return out


def deserialize_json(data: dict) -> UpdateReplicationInfoRequest:
    out: UpdateReplicationInfoRequest = {}  # type: ignore[typeddict-item]
    if "consumerGroupReplication" in data:
        import capo_kafka.types.consumer_group_replication_update

        out["consumer_group_replication"] = (
            capo_kafka.types.consumer_group_replication_update.deserialize_json(
                data["consumerGroupReplication"]
            )
        )
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    if "sourceKafkaClusterArn" in data:
        out["source_kafka_cluster_arn"] = data["sourceKafkaClusterArn"]
    if "sourceKafkaClusterId" in data:
        out["source_kafka_cluster_id"] = data["sourceKafkaClusterId"]
    if "targetKafkaClusterArn" in data:
        out["target_kafka_cluster_arn"] = data["targetKafkaClusterArn"]
    if "targetKafkaClusterId" in data:
        out["target_kafka_cluster_id"] = data["targetKafkaClusterId"]
    if "topicReplication" in data:
        import capo_kafka.types.topic_replication_update

        out["topic_replication"] = (
            capo_kafka.types.topic_replication_update.deserialize_json(
                data["topicReplication"]
            )
        )
    if "logDelivery" in data:
        import capo_kafka.types.log_delivery

        out["log_delivery"] = capo_kafka.types.log_delivery.deserialize_json(
            data["logDelivery"]
        )
    return out
