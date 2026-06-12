"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#SystemEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.event_type
    import aws_sdk_iot_events_data.types.state_change_configuration


class SystemEvent(TypedDict):
    event_type: NotRequired["aws_sdk_iot_events_data.types.event_type.EventType"]
    """<p>The event type. If the value is <code>STATE_CHANGE</code>, the event contains information about alarm state changes.</p>"""
    state_change_configuration: NotRequired[
        "aws_sdk_iot_events_data.types.state_change_configuration.StateChangeConfiguration"
    ]
    """<p>Contains the configuration information of alarm state changes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemEvent) -> dict:
    out: dict = {}
    if "event_type" in value:
        import aws_sdk_iot_events_data.types.event_type

        out["eventType"] = aws_sdk_iot_events_data.types.event_type.serialize_json(
            value["event_type"]
        )
    if "state_change_configuration" in value:
        import aws_sdk_iot_events_data.types.state_change_configuration

        out["stateChangeConfiguration"] = (
            aws_sdk_iot_events_data.types.state_change_configuration.serialize_json(
                value["state_change_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SystemEvent:
    out: SystemEvent = {}  # type: ignore[typeddict-item]
    if "eventType" in data:
        import aws_sdk_iot_events_data.types.event_type

        out["event_type"] = aws_sdk_iot_events_data.types.event_type.deserialize_json(
            data["eventType"]
        )
    if "stateChangeConfiguration" in data:
        import aws_sdk_iot_events_data.types.state_change_configuration

        out["state_change_configuration"] = (
            aws_sdk_iot_events_data.types.state_change_configuration.deserialize_json(
                data["stateChangeConfiguration"]
            )
        )
    return out
