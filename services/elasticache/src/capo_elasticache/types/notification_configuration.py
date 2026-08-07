"""Generated from Smithy shape ``com.amazonaws.elasticache#NotificationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string


class NotificationConfiguration(TypedDict, closed=True):
    topic_arn: NotRequired["capo_elasticache.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that identifies the topic.</p>"""
    topic_status: NotRequired["capo_elasticache.types.string.String"]
    """<p>The current state of the topic.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: NotificationConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "topic_arn" in value:
        pairs.append((f"{key_prefix}TopicArn", str(value["topic_arn"])))
    if "topic_status" in value:
        pairs.append((f"{key_prefix}TopicStatus", str(value["topic_status"])))


def deserialize_query(el: Element) -> NotificationConfiguration:
    out: NotificationConfiguration = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    child_topic_status = el.find("TopicStatus")
    if child_topic_status is not None:
        out["topic_status"] = str(child_topic_status.text or "")
    return out
