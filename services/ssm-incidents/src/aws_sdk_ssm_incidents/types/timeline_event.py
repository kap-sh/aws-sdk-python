"""Generated from Smithy shape ``com.amazonaws.ssmincidents#TimelineEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.event_data
    import aws_sdk_ssm_incidents.types.event_reference_list
    import aws_sdk_ssm_incidents.types.timeline_event_type
    import aws_sdk_ssm_incidents.types.uuid


class TimelineEvent(TypedDict):
    incident_record_arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident that the event occurred during.</p>"""
    event_id: "aws_sdk_ssm_incidents.types.uuid.UUID"
    """<p>The ID of the timeline event.</p>"""
    event_time: "datetime.datetime"
    """<p>The timestamp for when the event occurred.</p>"""
    event_updated_time: "datetime.datetime"
    """<p>The timestamp for when the timeline event was last updated.</p>"""
    event_type: "aws_sdk_ssm_incidents.types.timeline_event_type.TimelineEventType"
    """<p>The type of event that occurred. Currently Incident Manager supports only the <code>Custom Event</code> and <code>Note</code> types.</p>"""
    event_data: "aws_sdk_ssm_incidents.types.event_data.EventData"
    """<p>A short description of the event.</p>"""
    event_references: NotRequired[
        "aws_sdk_ssm_incidents.types.event_reference_list.EventReferenceList"
    ]
    """<p>A list of references in a <code>TimelineEvent</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimelineEvent) -> dict:
    out: dict = {}
    out["incidentRecordArn"] = value["incident_record_arn"]
    out["eventId"] = value["event_id"]
    import aws_sdk_ssm_incidents.types._prelude.timestamp

    out["eventTime"] = aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
        value["event_time"]
    )
    import aws_sdk_ssm_incidents.types._prelude.timestamp

    out["eventUpdatedTime"] = (
        aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
            value["event_updated_time"]
        )
    )
    out["eventType"] = value["event_type"]
    out["eventData"] = value["event_data"]
    if "event_references" in value:
        import aws_sdk_ssm_incidents.types.event_reference_list

        out["eventReferences"] = (
            aws_sdk_ssm_incidents.types.event_reference_list.serialize_json(
                value["event_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> TimelineEvent:
    out: TimelineEvent = {}  # type: ignore[typeddict-item]
    if "incidentRecordArn" in data:
        out["incident_record_arn"] = data["incidentRecordArn"]
    else:
        raise DeserializationError("TimelineEvent.incident_record_arn required")
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    else:
        raise DeserializationError("TimelineEvent.event_id required")
    if "eventTime" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["event_time"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["eventTime"]
            )
        )
    else:
        raise DeserializationError("TimelineEvent.event_time required")
    if "eventUpdatedTime" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["event_updated_time"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["eventUpdatedTime"]
            )
        )
    else:
        raise DeserializationError("TimelineEvent.event_updated_time required")
    if "eventType" in data:
        out["event_type"] = data["eventType"]
    else:
        raise DeserializationError("TimelineEvent.event_type required")
    if "eventData" in data:
        out["event_data"] = data["eventData"]
    else:
        raise DeserializationError("TimelineEvent.event_data required")
    if "eventReferences" in data:
        import aws_sdk_ssm_incidents.types.event_reference_list

        out["event_references"] = (
            aws_sdk_ssm_incidents.types.event_reference_list.deserialize_json(
                data["eventReferences"]
            )
        )
    return out
