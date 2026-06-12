"""Generated from Smithy shape ``com.amazonaws.kafka#TopicInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__integer
    import aws_sdk_kafka.types.__string


class TopicInfo(TypedDict):
    topic_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the topic.</p>"""
    topic_name: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>Name for a topic.</p>"""
    replication_factor: NotRequired["aws_sdk_kafka.types.__integer.__integer"]
    """<p>Replication factor for a topic.</p>"""
    partition_count: NotRequired["aws_sdk_kafka.types.__integer.__integer"]
    """<p>Partition count for a topic.</p>"""
    out_of_sync_replica_count: NotRequired["aws_sdk_kafka.types.__integer.__integer"]
    """<p>Number of out-of-sync replicas for a topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicInfo) -> dict:
    out: dict = {}
    if "topic_arn" in value:
        out["topicArn"] = value["topic_arn"]
    if "topic_name" in value:
        out["topicName"] = value["topic_name"]
    if "replication_factor" in value:
        out["replicationFactor"] = value["replication_factor"]
    if "partition_count" in value:
        out["partitionCount"] = value["partition_count"]
    if "out_of_sync_replica_count" in value:
        out["outOfSyncReplicaCount"] = value["out_of_sync_replica_count"]
    return out


def deserialize_json(data: dict) -> TopicInfo:
    out: TopicInfo = {}  # type: ignore[typeddict-item]
    if "topicArn" in data:
        out["topic_arn"] = data["topicArn"]
    if "topicName" in data:
        out["topic_name"] = data["topicName"]
    if "replicationFactor" in data:
        out["replication_factor"] = data["replicationFactor"]
    if "partitionCount" in data:
        out["partition_count"] = data["partitionCount"]
    if "outOfSyncReplicaCount" in data:
        out["out_of_sync_replica_count"] = data["outOfSyncReplicaCount"]
    return out
