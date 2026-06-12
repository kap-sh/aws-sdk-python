"""Generated from Smithy shape ``com.amazonaws.kafka#UpdateTopicRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__integer
    import aws_sdk_kafka.types.__string


class UpdateTopicRequest(TypedDict):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""
    topic_name: "aws_sdk_kafka.types.__string.__string"
    """<p>The name of the topic to update configuration for.</p>"""
    configs: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The new topic configurations encoded as a Base64 string.</p>"""
    partition_count: NotRequired["aws_sdk_kafka.types.__integer.__integer"]
    """<p>The new total number of partitions for the topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTopicRequest) -> dict:
    out: dict = {}
    if "configs" in value:
        out["configs"] = value["configs"]
    if "partition_count" in value:
        out["partitionCount"] = value["partition_count"]
    return out


def deserialize_json(data: dict) -> UpdateTopicRequest:
    out: UpdateTopicRequest = {}  # type: ignore[typeddict-item]
    if "configs" in data:
        out["configs"] = data["configs"]
    if "partitionCount" in data:
        out["partition_count"] = data["partitionCount"]
    return out
