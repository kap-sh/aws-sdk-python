"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RollbackAutomationEventRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.client_token
    import aws_sdk_compute_optimizer_automation.types.event_id


class RollbackAutomationEventRequest(TypedDict):
    event_id: "aws_sdk_compute_optimizer_automation.types.event_id.EventId"
    """<p> The ID of the automation event to roll back. </p>"""
    client_token: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RollbackAutomationEventRequest) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RollbackAutomationEventRequest:
    out: RollbackAutomationEventRequest = {}  # type: ignore[typeddict-item]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    else:
        raise DeserializationError("RollbackAutomationEventRequest.event_id required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
