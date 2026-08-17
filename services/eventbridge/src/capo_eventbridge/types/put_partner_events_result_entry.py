"""Generated from Smithy shape ``com.amazonaws.eventbridge#PutPartnerEventsResultEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.error_code
    import capo_eventbridge.types.error_message
    import capo_eventbridge.types.event_id


class PutPartnerEventsResultEntry(TypedDict, closed=True):
    event_id: NotRequired["capo_eventbridge.types.event_id.EventId"]
    """<p>The ID of the event.</p>"""
    error_code: NotRequired["capo_eventbridge.types.error_code.ErrorCode"]
    """<p>The error code that indicates why the event submission failed.</p>"""
    error_message: NotRequired["capo_eventbridge.types.error_message.ErrorMessage"]
    """<p>The error message that explains why the event submission failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPartnerEventsResultEntry) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["EventId"] = value["event_id"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutPartnerEventsResultEntry:
    out: PutPartnerEventsResultEntry = {}  # type: ignore[typeddict-item]
    if data.get("EventId") is not None:
        out["event_id"] = data["EventId"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
