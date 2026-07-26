"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeTopicResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__integer
    import capo_kafka.types.__string
    import capo_kafka.types.topic_state


class DescribeTopicResponse(TypedDict, closed=True):
    topic_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the topic.</p>"""
    topic_name: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Kafka topic name of the topic.</p>"""
    replication_factor: NotRequired["capo_kafka.types.__integer.__integer"]
    """<p>The replication factor of the topic.</p>"""
    partition_count: NotRequired["capo_kafka.types.__integer.__integer"]
    """<p>The partition count of the topic.</p>"""
    configs: NotRequired["capo_kafka.types.__string.__string"]
    """<p>Topic configurations encoded as a Base64 string.</p>"""
    status: NotRequired["capo_kafka.types.topic_state.TopicState"]
    """<p>The status of the topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTopicResponse) -> dict:
    out: dict = {}
    if "topic_arn" in value:
        out["topicArn"] = value["topic_arn"]
    if "topic_name" in value:
        out["topicName"] = value["topic_name"]
    if "replication_factor" in value:
        out["replicationFactor"] = value["replication_factor"]
    if "partition_count" in value:
        out["partitionCount"] = value["partition_count"]
    if "configs" in value:
        out["configs"] = value["configs"]
    if "status" in value:
        import capo_kafka.types.topic_state

        out["status"] = capo_kafka.types.topic_state.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> DescribeTopicResponse:
    out: DescribeTopicResponse = {}  # type: ignore[typeddict-item]
    if "topicArn" in data:
        out["topic_arn"] = data["topicArn"]
    if "topicName" in data:
        out["topic_name"] = data["topicName"]
    if "replicationFactor" in data:
        out["replication_factor"] = data["replicationFactor"]
    if "partitionCount" in data:
        out["partition_count"] = data["partitionCount"]
    if "configs" in data:
        out["configs"] = data["configs"]
    if "status" in data:
        import capo_kafka.types.topic_state

        out["status"] = capo_kafka.types.topic_state.deserialize_json(data["status"])
    return out
