"""Generated from Smithy shape ``com.amazonaws.kafka#CreateTopicResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__string
    import capo_kafka.types.topic_state


class CreateTopicResponse(TypedDict, closed=True):
    topic_arn: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the topic.</p>"""
    topic_name: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The name of the topic that was created.</p>"""
    status: NotRequired["capo_kafka.types.topic_state.TopicState"]
    """<p>The status of the topic creation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTopicResponse) -> dict:
    out: dict = {}
    if "topic_arn" in value:
        out["topicArn"] = value["topic_arn"]
    if "topic_name" in value:
        out["topicName"] = value["topic_name"]
    if "status" in value:
        import capo_kafka.types.topic_state

        out["status"] = capo_kafka.types.topic_state.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> CreateTopicResponse:
    out: CreateTopicResponse = {}  # type: ignore[typeddict-item]
    if "topicArn" in data:
        out["topic_arn"] = data["topicArn"]
    if "topicName" in data:
        out["topic_name"] = data["topicName"]
    if "status" in data:
        import capo_kafka.types.topic_state

        out["status"] = capo_kafka.types.topic_state.deserialize_json(data["status"])
    return out
