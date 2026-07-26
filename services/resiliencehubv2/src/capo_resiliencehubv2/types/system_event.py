"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SystemEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.event_actor
    import capo_resiliencehubv2.types.system_event_details
    import capo_resiliencehubv2.types.system_event_type
    import capo_resiliencehubv2.types.uuid


class SystemEvent(TypedDict, closed=True):
    event_id: "capo_resiliencehubv2.types.uuid.Uuid"
    """<p>The unique identifier of the event.</p>"""
    timestamp: "datetime.datetime"
    """<p>The timestamp of the event.</p>"""
    event_type: "capo_resiliencehubv2.types.system_event_type.SystemEventType"
    """<p>The type of the event.</p>"""
    system_arn: "capo_resiliencehubv2.types.arn.Arn"
    actor: "capo_resiliencehubv2.types.event_actor.EventActor"
    """<p>The actor that triggered the event.</p>"""
    event_details: "capo_resiliencehubv2.types.system_event_details.SystemEventDetails"
    """<p>The details of the event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemEvent) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    import capo_resiliencehubv2.types._prelude.timestamp

    out["timestamp"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    import capo_resiliencehubv2.types.system_event_type

    out["eventType"] = capo_resiliencehubv2.types.system_event_type.serialize_json(
        value["event_type"]
    )
    out["systemArn"] = value["system_arn"]
    import capo_resiliencehubv2.types.event_actor

    out["actor"] = capo_resiliencehubv2.types.event_actor.serialize_json(value["actor"])
    import capo_resiliencehubv2.types.system_event_details

    out["eventDetails"] = (
        capo_resiliencehubv2.types.system_event_details.serialize_json(
            value["event_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> SystemEvent:
    out: SystemEvent = {}  # type: ignore[typeddict-item]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    else:
        raise DeserializationError("SystemEvent.event_id required")
    if "timestamp" in data:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["timestamp"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        raise DeserializationError("SystemEvent.timestamp required")
    if "eventType" in data:
        import capo_resiliencehubv2.types.system_event_type

        out["event_type"] = (
            capo_resiliencehubv2.types.system_event_type.deserialize_json(
                data["eventType"]
            )
        )
    else:
        raise DeserializationError("SystemEvent.event_type required")
    if "systemArn" in data:
        out["system_arn"] = data["systemArn"]
    else:
        raise DeserializationError("SystemEvent.system_arn required")
    if "actor" in data:
        import capo_resiliencehubv2.types.event_actor

        out["actor"] = capo_resiliencehubv2.types.event_actor.deserialize_json(
            data["actor"]
        )
    else:
        raise DeserializationError("SystemEvent.actor required")
    if "eventDetails" in data:
        import capo_resiliencehubv2.types.system_event_details

        out["event_details"] = (
            capo_resiliencehubv2.types.system_event_details.deserialize_json(
                data["eventDetails"]
            )
        )
    else:
        raise DeserializationError("SystemEvent.event_details required")
    return out
