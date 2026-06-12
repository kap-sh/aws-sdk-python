"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteEventsByEventTypeResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.identifier
    import aws_sdk_frauddetector.types.string


class DeleteEventsByEventTypeResult(TypedDict):
    event_type_name: NotRequired["aws_sdk_frauddetector.types.identifier.identifier"]
    """<p>Name of event type for which to delete the events.</p>"""
    events_deletion_status: NotRequired["aws_sdk_frauddetector.types.string.string"]
    """<p>The status of the delete request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEventsByEventTypeResult) -> dict:
    out: dict = {}
    if "event_type_name" in value:
        out["eventTypeName"] = value["event_type_name"]
    if "events_deletion_status" in value:
        out["eventsDeletionStatus"] = value["events_deletion_status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEventsByEventTypeResult:
    out: DeleteEventsByEventTypeResult = {}  # type: ignore[typeddict-item]
    if "eventTypeName" in data:
        out["event_type_name"] = data["eventTypeName"]
    if "eventsDeletionStatus" in data:
        out["events_deletion_status"] = data["eventsDeletionStatus"]
    return out
