"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#DescribeEventBusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.event_bus_name_or_arn


class DescribeEventBusRequest(TypedDict):
    name: NotRequired[
        "aws_sdk_cloudwatch_events.types.event_bus_name_or_arn.EventBusNameOrArn"
    ]
    """<p>The name or ARN of the event bus to show details for. If you omit this, the default event bus is displayed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventBusRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventBusRequest:
    out: DescribeEventBusRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
