"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteEventRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.delete_audit_history
    import aws_sdk_frauddetector.types.identifier


class DeleteEventRequest(TypedDict):
    event_id: "aws_sdk_frauddetector.types.identifier.identifier"
    """<p>The ID of the event to delete.</p>"""
    event_type_name: "aws_sdk_frauddetector.types.identifier.identifier"
    """<p>The name of the event type.</p>"""
    delete_audit_history: NotRequired[
        "aws_sdk_frauddetector.types.delete_audit_history.DeleteAuditHistory"
    ]
    """<p>Specifies whether or not to delete any predictions associated with the event. If set to <code>True</code>, </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEventRequest) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    out["eventTypeName"] = value["event_type_name"]
    if "delete_audit_history" in value:
        out["deleteAuditHistory"] = value["delete_audit_history"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEventRequest:
    out: DeleteEventRequest = {}  # type: ignore[typeddict-item]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    else:
        raise DeserializationError("DeleteEventRequest.event_id required")
    if "eventTypeName" in data:
        out["event_type_name"] = data["eventTypeName"]
    else:
        raise DeserializationError("DeleteEventRequest.event_type_name required")
    if "deleteAuditHistory" in data:
        out["delete_audit_history"] = data["deleteAuditHistory"]
    return out
