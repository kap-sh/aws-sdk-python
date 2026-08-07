"""Generated from Smithy shape ``com.amazonaws.sns#CreateTopicResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.topic_arn


class CreateTopicResponse(TypedDict, closed=True):
    topic_arn: NotRequired["capo_sns.types.topic_arn.topicARN"]
    """<p>The Amazon Resource Name (ARN) assigned to the created topic.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateTopicResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "topic_arn" in value:
        pairs.append((f"{key_prefix}TopicArn", str(value["topic_arn"])))


def deserialize_query(el: Element) -> CreateTopicResponse:
    out: CreateTopicResponse = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    return out
