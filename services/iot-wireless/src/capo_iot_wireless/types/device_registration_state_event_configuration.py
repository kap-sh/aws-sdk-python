"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeviceRegistrationStateEventConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.event_notification_topic_status
    import capo_iot_wireless.types.sidewalk_event_notification_configurations


class DeviceRegistrationStateEventConfiguration(TypedDict, closed=True):
    sidewalk: NotRequired[
        "capo_iot_wireless.types.sidewalk_event_notification_configurations.SidewalkEventNotificationConfigurations"
    ]
    """<p>Device registration state event configuration object for enabling or disabling Sidewalk related event topics.</p>"""
    wireless_device_id_event_topic: NotRequired[
        "capo_iot_wireless.types.event_notification_topic_status.EventNotificationTopicStatus"
    ]
    """<p>Denotes whether the wireless device ID device registration state event topic is enabled or disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeviceRegistrationStateEventConfiguration) -> dict:
    out: dict = {}
    if "sidewalk" in value:
        import capo_iot_wireless.types.sidewalk_event_notification_configurations

        out["Sidewalk"] = (
            capo_iot_wireless.types.sidewalk_event_notification_configurations.serialize_json(
                value["sidewalk"]
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


def deserialize_json(data: dict) -> DeviceRegistrationStateEventConfiguration:
    out: DeviceRegistrationStateEventConfiguration = {}  # type: ignore[typeddict-item]
    if "Sidewalk" in data:
        import capo_iot_wireless.types.sidewalk_event_notification_configurations

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_event_notification_configurations.deserialize_json(
                data["Sidewalk"]
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
