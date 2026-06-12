"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANJoinEventNotificationConfigurations``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.event_notification_topic_status


class LoRaWANJoinEventNotificationConfigurations(TypedDict):
    dev_eui_event_topic: NotRequired[
        "aws_sdk_iot_wireless.types.event_notification_topic_status.EventNotificationTopicStatus"
    ]
    """<p>Denotes whether the Dev EUI join event topic is enabled or disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANJoinEventNotificationConfigurations) -> dict:
    out: dict = {}
    if "dev_eui_event_topic" in value:
        import aws_sdk_iot_wireless.types.event_notification_topic_status

        out["DevEuiEventTopic"] = (
            aws_sdk_iot_wireless.types.event_notification_topic_status.serialize_json(
                value["dev_eui_event_topic"]
            )
        )
    return out


def deserialize_json(data: dict) -> LoRaWANJoinEventNotificationConfigurations:
    out: LoRaWANJoinEventNotificationConfigurations = {}  # type: ignore[typeddict-item]
    if "DevEuiEventTopic" in data:
        import aws_sdk_iot_wireless.types.event_notification_topic_status

        out["dev_eui_event_topic"] = (
            aws_sdk_iot_wireless.types.event_notification_topic_status.deserialize_json(
                data["DevEuiEventTopic"]
            )
        )
    return out
