"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RollbackAutomationEventResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.event_id
    import aws_sdk_compute_optimizer_automation.types.event_status


class RollbackAutomationEventResponse(TypedDict, closed=True):
    event_id: NotRequired["aws_sdk_compute_optimizer_automation.types.event_id.EventId"]
    """<p> The ID of the automation event being rolled back. </p>"""
    event_status: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.event_status.EventStatus"
    ]
    """<p> The current status of the rollback operation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RollbackAutomationEventResponse) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    if "event_status" in value:
        import aws_sdk_compute_optimizer_automation.types.event_status

        out["eventStatus"] = (
            aws_sdk_compute_optimizer_automation.types.event_status.serialize_aws_json_1_0(
                value["event_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RollbackAutomationEventResponse:
    out: RollbackAutomationEventResponse = {}  # type: ignore[typeddict-item]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    if "eventStatus" in data:
        import aws_sdk_compute_optimizer_automation.types.event_status

        out["event_status"] = (
            aws_sdk_compute_optimizer_automation.types.event_status.deserialize_aws_json_1_0(
                data["eventStatus"]
            )
        )
    return out
