"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANConnectionStatusResourceTypeEventConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.event_notification_topic_status


class LoRaWANConnectionStatusResourceTypeEventConfiguration(TypedDict, closed=True):
    wireless_gateway_event_topic: NotRequired[
        "capo_iot_wireless.types.event_notification_topic_status.EventNotificationTopicStatus"
    ]
    """<p>Denotes whether the wireless gateway connection status event topic is enabled or disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: LoRaWANConnectionStatusResourceTypeEventConfiguration,
) -> dict:
    out: dict = {}
    if "wireless_gateway_event_topic" in value:
        import capo_iot_wireless.types.event_notification_topic_status

        out["WirelessGatewayEventTopic"] = (
            capo_iot_wireless.types.event_notification_topic_status.serialize_json(
                value["wireless_gateway_event_topic"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> LoRaWANConnectionStatusResourceTypeEventConfiguration:
    out: LoRaWANConnectionStatusResourceTypeEventConfiguration = {}  # type: ignore[typeddict-item]
    if "WirelessGatewayEventTopic" in data:
        import capo_iot_wireless.types.event_notification_topic_status

        out["wireless_gateway_event_topic"] = (
            capo_iot_wireless.types.event_notification_topic_status.deserialize_json(
                data["WirelessGatewayEventTopic"]
            )
        )
    return out
