"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#GetAutomationEventRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.event_id


class GetAutomationEventRequest(TypedDict):
    event_id: "aws_sdk_compute_optimizer_automation.types.event_id.EventId"
    """<p> The ID of the automation event to retrieve. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAutomationEventRequest) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAutomationEventRequest:
    out: GetAutomationEventRequest = {}  # type: ignore[typeddict-item]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    else:
        raise DeserializationError("GetAutomationEventRequest.event_id required")
    return out
