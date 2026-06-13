"""Generated from Smithy shape ``com.amazonaws.ssmincidents#DeleteTimelineEventInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.uuid


class DeleteTimelineEventInput(TypedDict):
    incident_record_arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident that includes the timeline event.</p>"""
    event_id: "aws_sdk_ssm_incidents.types.uuid.UUID"
    """<p>The ID of the event to update. You can use <code>ListTimelineEvents</code> to find an event's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTimelineEventInput) -> dict:
    out: dict = {}
    out["incidentRecordArn"] = value["incident_record_arn"]
    out["eventId"] = value["event_id"]
    return out


def deserialize_json(data: dict) -> DeleteTimelineEventInput:
    out: DeleteTimelineEventInput = {}  # type: ignore[typeddict-item]
    if "incidentRecordArn" in data:
        out["incident_record_arn"] = data["incidentRecordArn"]
    else:
        raise DeserializationError(
            "DeleteTimelineEventInput.incident_record_arn required"
        )
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    else:
        raise DeserializationError("DeleteTimelineEventInput.event_id required")
    return out
