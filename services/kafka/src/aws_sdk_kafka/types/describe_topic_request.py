"""Generated from Smithy shape ``com.amazonaws.kafka#DescribeTopicRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class DescribeTopicRequest(TypedDict, closed=True):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""
    topic_name: "aws_sdk_kafka.types.__string.__string"
    """<p>The Kafka topic name that uniquely identifies the topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTopicRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTopicRequest:
    out: DescribeTopicRequest = {}  # type: ignore[typeddict-item]
    return out
