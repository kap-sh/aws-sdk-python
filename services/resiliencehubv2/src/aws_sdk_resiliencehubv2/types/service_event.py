"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.event_actor
    import aws_sdk_resiliencehubv2.types.service_event_details
    import aws_sdk_resiliencehubv2.types.service_event_type
    import aws_sdk_resiliencehubv2.types.uuid


class ServiceEvent(TypedDict):
    event_id: "aws_sdk_resiliencehubv2.types.uuid.Uuid"
    """<p>The unique identifier of the event.</p>"""
    timestamp: "datetime.datetime"
    """<p>The timestamp of the event.</p>"""
    event_type: "aws_sdk_resiliencehubv2.types.service_event_type.ServiceEventType"
    """<p>The type of the event.</p>"""
    service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    actor: "aws_sdk_resiliencehubv2.types.event_actor.EventActor"
    """<p>The actor that triggered the event.</p>"""
    event_details: (
        "aws_sdk_resiliencehubv2.types.service_event_details.ServiceEventDetails"
    )
    """<p>The details of the event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceEvent) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    import aws_sdk_resiliencehubv2.types._prelude.timestamp

    out["timestamp"] = aws_sdk_resiliencehubv2.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    import aws_sdk_resiliencehubv2.types.service_event_type

    out["eventType"] = aws_sdk_resiliencehubv2.types.service_event_type.serialize_json(
        value["event_type"]
    )
    out["serviceArn"] = value["service_arn"]
    import aws_sdk_resiliencehubv2.types.event_actor

    out["actor"] = aws_sdk_resiliencehubv2.types.event_actor.serialize_json(
        value["actor"]
    )
    import aws_sdk_resiliencehubv2.types.service_event_details

    out["eventDetails"] = (
        aws_sdk_resiliencehubv2.types.service_event_details.serialize_json(
            value["event_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> ServiceEvent:
    out: ServiceEvent = {}  # type: ignore[typeddict-item]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    else:
        raise DeserializationError("ServiceEvent.event_id required")
    if "timestamp" in data:
        import aws_sdk_resiliencehubv2.types._prelude.timestamp

        out["timestamp"] = (
            aws_sdk_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        raise DeserializationError("ServiceEvent.timestamp required")
    if "eventType" in data:
        import aws_sdk_resiliencehubv2.types.service_event_type

        out["event_type"] = (
            aws_sdk_resiliencehubv2.types.service_event_type.deserialize_json(
                data["eventType"]
            )
        )
    else:
        raise DeserializationError("ServiceEvent.event_type required")
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError("ServiceEvent.service_arn required")
    if "actor" in data:
        import aws_sdk_resiliencehubv2.types.event_actor

        out["actor"] = aws_sdk_resiliencehubv2.types.event_actor.deserialize_json(
            data["actor"]
        )
    else:
        raise DeserializationError("ServiceEvent.actor required")
    if "eventDetails" in data:
        import aws_sdk_resiliencehubv2.types.service_event_details

        out["event_details"] = (
            aws_sdk_resiliencehubv2.types.service_event_details.deserialize_json(
                data["eventDetails"]
            )
        )
    else:
        raise DeserializationError("ServiceEvent.event_details required")
    return out
