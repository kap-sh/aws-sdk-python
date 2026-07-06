"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#CreateEventBusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.string


class CreateEventBusResponse(TypedDict, closed=True):
    event_bus_arn: NotRequired["aws_sdk_cloudwatch_events.types.string.String"]
    """<p>The ARN of the new event bus.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEventBusResponse) -> dict:
    out: dict = {}
    if "event_bus_arn" in value:
        out["EventBusArn"] = value["event_bus_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEventBusResponse:
    out: CreateEventBusResponse = {}  # type: ignore[typeddict-item]
    if "EventBusArn" in data:
        out["event_bus_arn"] = data["EventBusArn"]
    return out
