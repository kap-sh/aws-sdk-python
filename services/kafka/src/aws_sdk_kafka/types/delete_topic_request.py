"""Generated from Smithy shape ``com.amazonaws.kafka#DeleteTopicRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class DeleteTopicRequest(TypedDict):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""
    topic_name: "aws_sdk_kafka.types.__string.__string"
    """<p>The name of the topic to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTopicRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTopicRequest:
    out: DeleteTopicRequest = {}  # type: ignore[typeddict-item]
    return out
