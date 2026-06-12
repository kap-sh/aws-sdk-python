"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#DescribeEventBusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.string


class DescribeEventBusResponse(TypedDict):
    name: NotRequired["aws_sdk_cloudwatch_events.types.string.String"]
    """<p>The name of the event bus. Currently, this is always <code>default</code>.</p>"""
    arn: NotRequired["aws_sdk_cloudwatch_events.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the account permitted to write events to the current account.</p>"""
    policy: NotRequired["aws_sdk_cloudwatch_events.types.string.String"]
    """<p>The policy that enables the external account to send events to your account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventBusResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventBusResponse:
    out: DescribeEventBusResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
