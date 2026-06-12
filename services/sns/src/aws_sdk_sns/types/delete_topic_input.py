"""Generated from Smithy shape ``com.amazonaws.sns#DeleteTopicInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sns.types.topic_arn


class DeleteTopicInput(TypedDict):
    topic_arn: "aws_sdk_sns.types.topic_arn.topicARN"
    """<p>The ARN of the topic you want to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteTopicInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.TopicArn", str(value["topic_arn"])))


def deserialize_query(el: Element) -> DeleteTopicInput:
    out: DeleteTopicInput = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    else:
        raise DeserializationError("DeleteTopicInput.topic_arn required")
    return out
