"""Generated from Smithy shape ``com.amazonaws.kafka#DeleteTopicResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.topic_state


class DeleteTopicResponse(TypedDict):
    topic_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the topic.</p>"""
    topic_name: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The name of the topic that was deleted.</p>"""
    status: NotRequired["aws_sdk_kafka.types.topic_state.TopicState"]
    """<p>The status of the topic deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTopicResponse) -> dict:
    out: dict = {}
    if "topic_arn" in value:
        out["topicArn"] = value["topic_arn"]
    if "topic_name" in value:
        out["topicName"] = value["topic_name"]
    if "status" in value:
        import aws_sdk_kafka.types.topic_state

        out["status"] = aws_sdk_kafka.types.topic_state.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> DeleteTopicResponse:
    out: DeleteTopicResponse = {}  # type: ignore[typeddict-item]
    if "topicArn" in data:
        out["topic_arn"] = data["topicArn"]
    if "topicName" in data:
        out["topic_name"] = data["topicName"]
    if "status" in data:
        import aws_sdk_kafka.types.topic_state

        out["status"] = aws_sdk_kafka.types.topic_state.deserialize_json(data["status"])
    return out
