"""Generated from Smithy shape ``com.amazonaws.elasticache#NotificationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string


class NotificationConfiguration(TypedDict):
    topic_arn: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that identifies the topic.</p>"""
    topic_status: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The current state of the topic.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: NotificationConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "topic_arn" in value:
        pairs.append((f"{prefix}.TopicArn", str(value["topic_arn"])))
    if "topic_status" in value:
        pairs.append((f"{prefix}.TopicStatus", str(value["topic_status"])))


def deserialize_query(el: Element) -> NotificationConfiguration:
    out: NotificationConfiguration = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    child_topic_status = el.find("TopicStatus")
    if child_topic_status is not None:
        out["topic_status"] = str(child_topic_status.text or "")
    return out
