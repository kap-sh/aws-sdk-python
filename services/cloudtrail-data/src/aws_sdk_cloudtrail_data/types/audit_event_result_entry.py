"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#AuditEventResultEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudtrail_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail_data.types.uuid


class AuditEventResultEntry(TypedDict, closed=True):
    id: "aws_sdk_cloudtrail_data.types.uuid.Uuid"
    """<p>The original event ID from the source event.</p>"""
    event_id: "aws_sdk_cloudtrail_data.types.uuid.Uuid"
    """<p>The event ID assigned by CloudTrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditEventResultEntry) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["eventID"] = value["event_id"]
    return out


def deserialize_json(data: dict) -> AuditEventResultEntry:
    out: AuditEventResultEntry = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AuditEventResultEntry.id required")
    if "eventID" in data:
        out["event_id"] = data["eventID"]
    else:
        raise DeserializationError("AuditEventResultEntry.event_id required")
    return out
