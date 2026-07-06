"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#EventBus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.string


class EventBus(TypedDict, closed=True):
    name: NotRequired["aws_sdk_cloudwatch_events.types.string.String"]
    """<p>The name of the event bus.</p>"""
    arn: NotRequired["aws_sdk_cloudwatch_events.types.string.String"]
    """<p>The ARN of the event bus.</p>"""
    policy: NotRequired["aws_sdk_cloudwatch_events.types.string.String"]
    """<p>The permissions policy of the event bus, describing which other Amazon Web Services accounts can write events to this event bus.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventBus) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EventBus:
    out: EventBus = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
