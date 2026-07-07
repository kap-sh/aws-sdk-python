"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#DescribePartnerEventSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.string


class DescribePartnerEventSourceResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_cloudwatch_events.types.string.String"]
    """<p>The ARN of the event source.</p>"""
    name: NotRequired["aws_sdk_cloudwatch_events.types.string.String"]
    """<p>The name of the event source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePartnerEventSourceResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePartnerEventSourceResponse:
    out: DescribePartnerEventSourceResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
