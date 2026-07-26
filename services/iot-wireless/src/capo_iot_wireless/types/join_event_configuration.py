"""Generated from Smithy shape ``com.amazonaws.iotwireless#JoinEventConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.event_notification_topic_status
    import capo_iot_wireless.types.lo_ra_wan_join_event_notification_configurations


class JoinEventConfiguration(TypedDict, closed=True):
    lo_ra_wan: NotRequired[
        "capo_iot_wireless.types.lo_ra_wan_join_event_notification_configurations.LoRaWANJoinEventNotificationConfigurations"
    ]
    """<p>Join event configuration object for enabling or disabling LoRaWAN related event topics.</p>"""
    wireless_device_id_event_topic: NotRequired[
        "capo_iot_wireless.types.event_notification_topic_status.EventNotificationTopicStatus"
    ]
    """<p>Denotes whether the wireless device ID join event topic is enabled or disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JoinEventConfiguration) -> dict:
    out: dict = {}
    if "lo_ra_wan" in value:
        import capo_iot_wireless.types.lo_ra_wan_join_event_notification_configurations

        out["LoRaWAN"] = (
            capo_iot_wireless.types.lo_ra_wan_join_event_notification_configurations.serialize_json(
                value["lo_ra_wan"]
            )
        )
    if "wireless_device_id_event_topic" in value:
        import capo_iot_wireless.types.event_notification_topic_status

        out["WirelessDeviceIdEventTopic"] = (
            capo_iot_wireless.types.event_notification_topic_status.serialize_json(
                value["wireless_device_id_event_topic"]
            )
        )
    return out


def deserialize_json(data: dict) -> JoinEventConfiguration:
    out: JoinEventConfiguration = {}  # type: ignore[typeddict-item]
    if "LoRaWAN" in data:
        import capo_iot_wireless.types.lo_ra_wan_join_event_notification_configurations

        out["lo_ra_wan"] = (
            capo_iot_wireless.types.lo_ra_wan_join_event_notification_configurations.deserialize_json(
                data["LoRaWAN"]
            )
        )
    if "WirelessDeviceIdEventTopic" in data:
        import capo_iot_wireless.types.event_notification_topic_status

        out["wireless_device_id_event_topic"] = (
            capo_iot_wireless.types.event_notification_topic_status.deserialize_json(
                data["WirelessDeviceIdEventTopic"]
            )
        )
    return out
