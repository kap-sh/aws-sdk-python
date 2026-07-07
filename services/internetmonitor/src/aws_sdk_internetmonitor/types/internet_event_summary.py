"""Generated from Smithy shape ``com.amazonaws.internetmonitor#InternetEventSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_internetmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_internetmonitor.types.arn
    import aws_sdk_internetmonitor.types.client_location
    import aws_sdk_internetmonitor.types.internet_event_id
    import aws_sdk_internetmonitor.types.internet_event_status
    import aws_sdk_internetmonitor.types.internet_event_type


class InternetEventSummary(TypedDict, closed=True):
    event_id: "aws_sdk_internetmonitor.types.internet_event_id.InternetEventId"
    """<p>The internally-generated identifier of an internet event.</p>"""
    event_arn: "aws_sdk_internetmonitor.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the internet event.</p>"""
    started_at: "datetime.datetime"
    """<p>The time when an internet event started.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The time when an internet event ended. If the event hasn't ended yet, this value is empty.</p>"""
    client_location: "aws_sdk_internetmonitor.types.client_location.ClientLocation"
    """<p>The impacted location, such as a city, that Amazon Web Services clients access application resources from.</p>"""
    event_type: "aws_sdk_internetmonitor.types.internet_event_type.InternetEventType"
    """<p>The type of network impairment.</p>"""
    event_status: (
        "aws_sdk_internetmonitor.types.internet_event_status.InternetEventStatus"
    )
    """<p>The status of an internet event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternetEventSummary) -> dict:
    out: dict = {}
    out["EventId"] = value["event_id"]
    out["EventArn"] = value["event_arn"]
    import aws_sdk_internetmonitor.types._prelude.timestamp

    out["StartedAt"] = aws_sdk_internetmonitor.types._prelude.timestamp.serialize_json(
        value["started_at"]
    )
    if "ended_at" in value:
        import aws_sdk_internetmonitor.types._prelude.timestamp

        out["EndedAt"] = (
            aws_sdk_internetmonitor.types._prelude.timestamp.serialize_json(
                value["ended_at"]
            )
        )
    import aws_sdk_internetmonitor.types.client_location

    out["ClientLocation"] = (
        aws_sdk_internetmonitor.types.client_location.serialize_json(
            value["client_location"]
        )
    )
    out["EventType"] = value["event_type"]
    out["EventStatus"] = value["event_status"]
    return out


def deserialize_json(data: dict) -> InternetEventSummary:
    out: InternetEventSummary = {}  # type: ignore[typeddict-item]
    if "EventId" in data:
        out["event_id"] = data["EventId"]
    else:
        raise DeserializationError("InternetEventSummary.event_id required")
    if "EventArn" in data:
        out["event_arn"] = data["EventArn"]
    else:
        raise DeserializationError("InternetEventSummary.event_arn required")
    if "StartedAt" in data:
        import aws_sdk_internetmonitor.types._prelude.timestamp

        out["started_at"] = (
            aws_sdk_internetmonitor.types._prelude.timestamp.deserialize_json(
                data["StartedAt"]
            )
        )
    else:
        raise DeserializationError("InternetEventSummary.started_at required")
    if "EndedAt" in data:
        import aws_sdk_internetmonitor.types._prelude.timestamp

        out["ended_at"] = (
            aws_sdk_internetmonitor.types._prelude.timestamp.deserialize_json(
                data["EndedAt"]
            )
        )
    if "ClientLocation" in data:
        import aws_sdk_internetmonitor.types.client_location

        out["client_location"] = (
            aws_sdk_internetmonitor.types.client_location.deserialize_json(
                data["ClientLocation"]
            )
        )
    else:
        raise DeserializationError("InternetEventSummary.client_location required")
    if "EventType" in data:
        out["event_type"] = data["EventType"]
    else:
        raise DeserializationError("InternetEventSummary.event_type required")
    if "EventStatus" in data:
        out["event_status"] = data["EventStatus"]
    else:
        raise DeserializationError("InternetEventSummary.event_status required")
    return out
