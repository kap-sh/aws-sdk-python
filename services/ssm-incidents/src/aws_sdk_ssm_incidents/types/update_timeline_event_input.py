"""Generated from Smithy shape ``com.amazonaws.ssmincidents#UpdateTimelineEventInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.client_token
    import aws_sdk_ssm_incidents.types.event_data
    import aws_sdk_ssm_incidents.types.event_reference_list
    import aws_sdk_ssm_incidents.types.timeline_event_type
    import aws_sdk_ssm_incidents.types.uuid


class UpdateTimelineEventInput(TypedDict):
    client_token: NotRequired["aws_sdk_ssm_incidents.types.client_token.ClientToken"]
    """<p>A token that ensures that a client calls the operation only once with the specified details.</p>"""
    incident_record_arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident that includes the timeline event.</p>"""
    event_id: "aws_sdk_ssm_incidents.types.uuid.UUID"
    """<p>The ID of the event to update. You can use <code>ListTimelineEvents</code> to find an event's ID.</p>"""
    event_time: NotRequired["datetime.datetime"]
    """<p>The timestamp for when the event occurred.</p>"""
    event_type: NotRequired[
        "aws_sdk_ssm_incidents.types.timeline_event_type.TimelineEventType"
    ]
    """<p>The type of event. You can update events of type <code>Custom Event</code> and <code>Note</code>.</p>"""
    event_data: NotRequired["aws_sdk_ssm_incidents.types.event_data.EventData"]
    """<p>A short description of the event.</p>"""
    event_references: NotRequired[
        "aws_sdk_ssm_incidents.types.event_reference_list.EventReferenceList"
    ]
    """<p>Updates all existing references in a <code>TimelineEvent</code>. A reference is an Amazon Web Services resource involved or associated with the incident. To specify a reference, enter its Amazon Resource Name (ARN). You can also specify a related item associated with that resource. For example, to specify an Amazon DynamoDB (DynamoDB) table as a resource, use its ARN. You can also specify an Amazon CloudWatch metric associated with the DynamoDB table as a related item.</p> <important> <p>This update action overrides all existing references. If you want to keep existing references, you must specify them in the call. If you don't, this action removes any existing references and enters only new references.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTimelineEventInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["incidentRecordArn"] = value["incident_record_arn"]
    out["eventId"] = value["event_id"]
    if "event_time" in value:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["eventTime"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
                value["event_time"]
            )
        )
    if "event_type" in value:
        out["eventType"] = value["event_type"]
    if "event_data" in value:
        out["eventData"] = value["event_data"]
    if "event_references" in value:
        import aws_sdk_ssm_incidents.types.event_reference_list

        out["eventReferences"] = (
            aws_sdk_ssm_incidents.types.event_reference_list.serialize_json(
                value["event_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateTimelineEventInput:
    out: UpdateTimelineEventInput = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "incidentRecordArn" in data:
        out["incident_record_arn"] = data["incidentRecordArn"]
    else:
        raise DeserializationError(
            "UpdateTimelineEventInput.incident_record_arn required"
        )
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    else:
        raise DeserializationError("UpdateTimelineEventInput.event_id required")
    if "eventTime" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["event_time"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["eventTime"]
            )
        )
    if "eventType" in data:
        out["event_type"] = data["eventType"]
    if "eventData" in data:
        out["event_data"] = data["eventData"]
    if "eventReferences" in data:
        import aws_sdk_ssm_incidents.types.event_reference_list

        out["event_references"] = (
            aws_sdk_ssm_incidents.types.event_reference_list.deserialize_json(
                data["eventReferences"]
            )
        )
    return out
