"""Generated from Smithy shape ``com.amazonaws.kafka#CreateTopicRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__integer_min1
    import aws_sdk_kafka.types.__string


class CreateTopicRequest(TypedDict, closed=True):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""
    topic_name: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The name of the topic to create.</p>"""
    partition_count: NotRequired["aws_sdk_kafka.types.__integer_min1.__integerMin1"]
    """<p>The number of partitions for the topic.</p>"""
    replication_factor: NotRequired["aws_sdk_kafka.types.__integer_min1.__integerMin1"]
    """<p>The replication factor for the topic.</p>"""
    configs: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>Topic configurations encoded as a Base64 string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTopicRequest) -> dict:
    out: dict = {}
    if "topic_name" in value:
        out["topicName"] = value["topic_name"]
    if "partition_count" in value:
        out["partitionCount"] = value["partition_count"]
    if "replication_factor" in value:
        out["replicationFactor"] = value["replication_factor"]
    if "configs" in value:
        out["configs"] = value["configs"]
    return out


def deserialize_json(data: dict) -> CreateTopicRequest:
    out: CreateTopicRequest = {}  # type: ignore[typeddict-item]
    if "topicName" in data:
        out["topic_name"] = data["topicName"]
    if "partitionCount" in data:
        out["partition_count"] = data["partitionCount"]
    if "replicationFactor" in data:
        out["replication_factor"] = data["replicationFactor"]
    if "configs" in data:
        out["configs"] = data["configs"]
    return out
