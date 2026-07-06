"""Generated from Smithy shape ``com.amazonaws.sns#Topic``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.topic_arn


class Topic(TypedDict, closed=True):
    topic_arn: NotRequired["aws_sdk_sns.types.topic_arn.topicARN"]
    """<p>The topic's ARN.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Topic, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "topic_arn" in value:
        pairs.append((f"{prefix}.TopicArn", str(value["topic_arn"])))


def deserialize_query(el: Element) -> Topic:
    out: Topic = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    return out
