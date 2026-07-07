"""Generated from Smithy shape ``com.amazonaws.ssmincidents#CreateTimelineEventInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.client_token
    import aws_sdk_ssm_incidents.types.event_data
    import aws_sdk_ssm_incidents.types.event_reference_list
    import aws_sdk_ssm_incidents.types.timeline_event_type


class CreateTimelineEventInput(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_ssm_incidents.types.client_token.ClientToken"]
    """<p>A token that ensures that a client calls the action only once with the specified details.</p>"""
    incident_record_arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident record that the action adds the incident to.</p>"""
    event_time: "datetime.datetime"
    """<p>The timestamp for when the event occurred.</p>"""
    event_type: "aws_sdk_ssm_incidents.types.timeline_event_type.TimelineEventType"
    """<p>The type of event. You can create timeline events of type <code>Custom Event</code> and <code>Note</code>.</p> <p>To make a Note-type event appear on the <i>Incident notes</i> panel in the console, specify <code>eventType</code> as <code>Note</code>and enter the Amazon Resource Name (ARN) of the incident as the value for <code>eventReference</code>.</p>"""
    event_data: "aws_sdk_ssm_incidents.types.event_data.EventData"
    """<p>A short description of the event.</p>"""
    event_references: NotRequired[
        "aws_sdk_ssm_incidents.types.event_reference_list.EventReferenceList"
    ]
    """<p>Adds one or more references to the <code>TimelineEvent</code>. A reference is an Amazon Web Services resource involved or associated with the incident. To specify a reference, enter its Amazon Resource Name (ARN). You can also specify a related item associated with a resource. For example, to specify an Amazon DynamoDB (DynamoDB) table as a resource, use the table's ARN. You can also specify an Amazon CloudWatch metric associated with the DynamoDB table as a related item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTimelineEventInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["incidentRecordArn"] = value["incident_record_arn"]
    import aws_sdk_ssm_incidents.types._prelude.timestamp

    out["eventTime"] = aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
        value["event_time"]
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


def deserialize_json(data: dict) -> CreateTimelineEventInput:
    out: CreateTimelineEventInput = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "incidentRecordArn" in data:
        out["incident_record_arn"] = data["incidentRecordArn"]
    else:
        raise DeserializationError(
            "CreateTimelineEventInput.incident_record_arn required"
        )
    if "eventTime" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["event_time"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["eventTime"]
            )
        )
    else:
        raise DeserializationError("CreateTimelineEventInput.event_time required")
    if "eventType" in data:
        out["event_type"] = data["eventType"]
    else:
        raise DeserializationError("CreateTimelineEventInput.event_type required")
    if "eventData" in data:
        out["event_data"] = data["eventData"]
    else:
        raise DeserializationError("CreateTimelineEventInput.event_data required")
    if "eventReferences" in data:
        import aws_sdk_ssm_incidents.types.event_reference_list

        out["event_references"] = (
            aws_sdk_ssm_incidents.types.event_reference_list.deserialize_json(
                data["eventReferences"]
            )
        )
    return out
