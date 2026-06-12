"""Generated from Smithy shape ``com.amazonaws.devopsguru#SnsChannelConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.topic_arn


class SnsChannelConfig(TypedDict):
    topic_arn: NotRequired["aws_sdk_devops_guru.types.topic_arn.TopicArn"]
    """<p> The Amazon Resource Name (ARN) of an Amazon Simple Notification Service topic. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnsChannelConfig) -> dict:
    out: dict = {}
    if "topic_arn" in value:
        out["TopicArn"] = value["topic_arn"]
    return out


def deserialize_json(data: dict) -> SnsChannelConfig:
    out: SnsChannelConfig = {}  # type: ignore[typeddict-item]
    if "TopicArn" in data:
        out["topic_arn"] = data["TopicArn"]
    return out
