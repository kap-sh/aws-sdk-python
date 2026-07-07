"""Generated from Smithy shape ``com.amazonaws.ec2#HistoryRecordEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.event_information
    import aws_sdk_ec2.types.fleet_event_type


class HistoryRecordEntry(TypedDict, closed=True):
    event_information: NotRequired[
        "aws_sdk_ec2.types.event_information.EventInformation"
    ]
    """<p>Information about the event.</p>"""
    event_type: NotRequired["aws_sdk_ec2.types.fleet_event_type.FleetEventType"]
    """<p>The event type.</p>"""
    timestamp: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time of the event, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: HistoryRecordEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "event_information" in value:
        import aws_sdk_ec2.types.event_information

        aws_sdk_ec2.types.event_information.serialize_ec2_query(
            value["event_information"], pairs, f"{prefix}.EventInformation"
        )
    if "event_type" in value:
        import aws_sdk_ec2.types.fleet_event_type

        aws_sdk_ec2.types.fleet_event_type.serialize_ec2_query(
            value["event_type"], pairs, f"{prefix}.EventType"
        )
    if "timestamp" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["timestamp"], pairs, f"{prefix}.Timestamp"
        )


def deserialize_ec2_query(el: Element) -> HistoryRecordEntry:
    out: HistoryRecordEntry = {}  # type: ignore[typeddict-item]
    child_event_information = el.find("EventInformation")
    if child_event_information is not None:
        import aws_sdk_ec2.types.event_information

        out["event_information"] = (
            aws_sdk_ec2.types.event_information.deserialize_ec2_query(
                child_event_information
            )
        )
    child_event_type = el.find("EventType")
    if child_event_type is not None:
        import aws_sdk_ec2.types.fleet_event_type

        out["event_type"] = aws_sdk_ec2.types.fleet_event_type.deserialize_ec2_query(
            child_event_type
        )
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import aws_sdk_ec2.types.date_time

        out["timestamp"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_timestamp
        )
    return out
