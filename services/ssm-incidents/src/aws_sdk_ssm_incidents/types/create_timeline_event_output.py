"""Generated from Smithy shape ``com.amazonaws.ssmincidents#CreateTimelineEventOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.uuid


class CreateTimelineEventOutput(TypedDict):
    incident_record_arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The ARN of the incident record that you added the event to.</p>"""
    event_id: "aws_sdk_ssm_incidents.types.uuid.UUID"
    """<p>The ID of the event for easy reference later. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTimelineEventOutput) -> dict:
    out: dict = {}
    out["incidentRecordArn"] = value["incident_record_arn"]
    out["eventId"] = value["event_id"]
    return out


def deserialize_json(data: dict) -> CreateTimelineEventOutput:
    out: CreateTimelineEventOutput = {}  # type: ignore[typeddict-item]
    if "incidentRecordArn" in data:
        out["incident_record_arn"] = data["incidentRecordArn"]
    else:
        raise DeserializationError(
            "CreateTimelineEventOutput.incident_record_arn required"
        )
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    else:
        raise DeserializationError("CreateTimelineEventOutput.event_id required")
    return out
