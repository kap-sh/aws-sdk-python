"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANConnectionStatusEventNotificationConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.event_notification_topic_status


class LoRaWANConnectionStatusEventNotificationConfigurations(TypedDict, closed=True):
    gateway_eui_event_topic: NotRequired[
        "capo_iot_wireless.types.event_notification_topic_status.EventNotificationTopicStatus"
    ]
    """<p>Denotes whether the gateway EUI connection status event topic is enabled or disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: LoRaWANConnectionStatusEventNotificationConfigurations,
) -> dict:
    out: dict = {}
    if "gateway_eui_event_topic" in value:
        import capo_iot_wireless.types.event_notification_topic_status

        out["GatewayEuiEventTopic"] = (
            capo_iot_wireless.types.event_notification_topic_status.serialize_json(
                value["gateway_eui_event_topic"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> LoRaWANConnectionStatusEventNotificationConfigurations:
    out: LoRaWANConnectionStatusEventNotificationConfigurations = {}  # type: ignore[typeddict-item]
    if "GatewayEuiEventTopic" in data:
        import capo_iot_wireless.types.event_notification_topic_status

        out["gateway_eui_event_topic"] = (
            capo_iot_wireless.types.event_notification_topic_status.deserialize_json(
                data["GatewayEuiEventTopic"]
            )
        )
    return out
