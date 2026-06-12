"""Generated from Smithy shape ``com.amazonaws.dax#NotificationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dax.types.string


class NotificationConfiguration(TypedDict):
    topic_arn: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that identifies the topic.</p>"""
    topic_status: NotRequired["aws_sdk_dax.types.string.String"]
    """<p>The current state of the topic. A value of “active” means that notifications will be sent to the topic. A value of “inactive” means that notifications will not be sent to the topic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationConfiguration) -> dict:
    out: dict = {}
    if "topic_arn" in value:
        out["TopicArn"] = value["topic_arn"]
    if "topic_status" in value:
        out["TopicStatus"] = value["topic_status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotificationConfiguration:
    out: NotificationConfiguration = {}  # type: ignore[typeddict-item]
    if "TopicArn" in data:
        out["topic_arn"] = data["TopicArn"]
    if "TopicStatus" in data:
        out["topic_status"] = data["TopicStatus"]
    return out
