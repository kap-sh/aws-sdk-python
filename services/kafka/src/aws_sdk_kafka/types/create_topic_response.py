"""Generated from Smithy shape ``com.amazonaws.kafka#CreateTopicResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.topic_state


class CreateTopicResponse(TypedDict):
    topic_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the topic.</p>"""
    topic_name: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The name of the topic that was created.</p>"""
    status: NotRequired["aws_sdk_kafka.types.topic_state.TopicState"]
    """<p>The status of the topic creation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTopicResponse) -> dict:
    out: dict = {}
    if "topic_arn" in value:
        out["topicArn"] = value["topic_arn"]
    if "topic_name" in value:
        out["topicName"] = value["topic_name"]
    if "status" in value:
        import aws_sdk_kafka.types.topic_state

        out["status"] = aws_sdk_kafka.types.topic_state.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> CreateTopicResponse:
    out: CreateTopicResponse = {}  # type: ignore[typeddict-item]
    if "topicArn" in data:
        out["topic_arn"] = data["topicArn"]
    if "topicName" in data:
        out["topic_name"] = data["topicName"]
    if "status" in data:
        import aws_sdk_kafka.types.topic_state

        out["status"] = aws_sdk_kafka.types.topic_state.deserialize_json(data["status"])
    return out
