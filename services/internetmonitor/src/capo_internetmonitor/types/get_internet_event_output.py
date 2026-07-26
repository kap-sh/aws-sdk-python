"""Generated from Smithy shape ``com.amazonaws.internetmonitor#GetInternetEventOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_internetmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_internetmonitor.types.arn
    import capo_internetmonitor.types.client_location
    import capo_internetmonitor.types.internet_event_id
    import capo_internetmonitor.types.internet_event_status
    import capo_internetmonitor.types.internet_event_type


class GetInternetEventOutput(TypedDict, closed=True):
    event_id: "capo_internetmonitor.types.internet_event_id.InternetEventId"
    """<p>The internally-generated identifier of an internet event.</p>"""
    event_arn: "capo_internetmonitor.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the internet event.</p>"""
    started_at: "datetime.datetime"
    """<p>The time when the internet event started.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The time when the internet event ended. If the event hasn't ended yet, this value is empty.</p>"""
    client_location: "capo_internetmonitor.types.client_location.ClientLocation"
    """<p>The impacted location, such as a city, where clients access Amazon Web Services application resources.</p>"""
    event_type: "capo_internetmonitor.types.internet_event_type.InternetEventType"
    """<p>The type of network impairment.</p>"""
    event_status: "capo_internetmonitor.types.internet_event_status.InternetEventStatus"
    """<p>The status of the internet event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInternetEventOutput) -> dict:
    out: dict = {}
    out["EventId"] = value["event_id"]
    out["EventArn"] = value["event_arn"]
    import capo_internetmonitor.types._prelude.timestamp

    out["StartedAt"] = capo_internetmonitor.types._prelude.timestamp.serialize_json(
        value["started_at"]
    )
    if "ended_at" in value:
        import capo_internetmonitor.types._prelude.timestamp

        out["EndedAt"] = capo_internetmonitor.types._prelude.timestamp.serialize_json(
            value["ended_at"]
        )
    import capo_internetmonitor.types.client_location

    out["ClientLocation"] = capo_internetmonitor.types.client_location.serialize_json(
        value["client_location"]
    )
    out["EventType"] = value["event_type"]
    out["EventStatus"] = value["event_status"]
    return out


def deserialize_json(data: dict) -> GetInternetEventOutput:
    out: GetInternetEventOutput = {}  # type: ignore[typeddict-item]
    if "EventId" in data:
        out["event_id"] = data["EventId"]
    else:
        raise DeserializationError("GetInternetEventOutput.event_id required")
    if "EventArn" in data:
        out["event_arn"] = data["EventArn"]
    else:
        raise DeserializationError("GetInternetEventOutput.event_arn required")
    if "StartedAt" in data:
        import capo_internetmonitor.types._prelude.timestamp

        out["started_at"] = (
            capo_internetmonitor.types._prelude.timestamp.deserialize_json(
                data["StartedAt"]
            )
        )
    else:
        raise DeserializationError("GetInternetEventOutput.started_at required")
    if "EndedAt" in data:
        import capo_internetmonitor.types._prelude.timestamp

        out["ended_at"] = (
            capo_internetmonitor.types._prelude.timestamp.deserialize_json(
                data["EndedAt"]
            )
        )
    if "ClientLocation" in data:
        import capo_internetmonitor.types.client_location

        out["client_location"] = (
            capo_internetmonitor.types.client_location.deserialize_json(
                data["ClientLocation"]
            )
        )
    else:
        raise DeserializationError("GetInternetEventOutput.client_location required")
    if "EventType" in data:
        out["event_type"] = data["EventType"]
    else:
        raise DeserializationError("GetInternetEventOutput.event_type required")
    if "EventStatus" in data:
        out["event_status"] = data["EventStatus"]
    else:
        raise DeserializationError("GetInternetEventOutput.event_status required")
    return out
