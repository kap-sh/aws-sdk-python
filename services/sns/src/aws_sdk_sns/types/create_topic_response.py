"""Generated from Smithy shape ``com.amazonaws.sns#CreateTopicResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.topic_arn


class CreateTopicResponse(TypedDict):
    topic_arn: NotRequired["aws_sdk_sns.types.topic_arn.topicARN"]
    """<p>The Amazon Resource Name (ARN) assigned to the created topic.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateTopicResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "topic_arn" in value:
        pairs.append((f"{prefix}.TopicArn", str(value["topic_arn"])))


def deserialize_query(el: Element) -> CreateTopicResponse:
    out: CreateTopicResponse = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    return out
