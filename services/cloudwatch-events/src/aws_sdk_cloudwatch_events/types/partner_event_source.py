"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PartnerEventSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.string


class PartnerEventSource(TypedDict):
    arn: NotRequired["aws_sdk_cloudwatch_events.types.string.String"]
    """<p>The ARN of the partner event source.</p>"""
    name: NotRequired["aws_sdk_cloudwatch_events.types.string.String"]
    """<p>The name of the partner event source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartnerEventSource) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PartnerEventSource:
    out: PartnerEventSource = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
