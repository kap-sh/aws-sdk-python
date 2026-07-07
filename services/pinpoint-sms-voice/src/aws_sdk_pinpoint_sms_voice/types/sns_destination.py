"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#SnsDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice.types.string


class SnsDestination(TypedDict, closed=True):
    topic_arn: NotRequired["aws_sdk_pinpoint_sms_voice.types.string.String"]
    """The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish events to."""


# --- restJson1 ser/de ---
def serialize_json(value: SnsDestination) -> dict:
    out: dict = {}
    if "topic_arn" in value:
        out["TopicArn"] = value["topic_arn"]
    return out


def deserialize_json(data: dict) -> SnsDestination:
    out: SnsDestination = {}  # type: ignore[typeddict-item]
    if "TopicArn" in data:
        out["topic_arn"] = data["TopicArn"]
    return out
