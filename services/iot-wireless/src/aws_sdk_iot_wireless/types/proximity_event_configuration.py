"""Generated from Smithy shape ``com.amazonaws.iotwireless#ProximityEventConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.event_notification_topic_status
    import aws_sdk_iot_wireless.types.sidewalk_event_notification_configurations


class ProximityEventConfiguration(TypedDict, closed=True):
    sidewalk: NotRequired[
        "aws_sdk_iot_wireless.types.sidewalk_event_notification_configurations.SidewalkEventNotificationConfigurations"
    ]
    """<p>Proximity event configuration object for enabling or disabling Sidewalk related event topics.</p>"""
    wireless_device_id_event_topic: NotRequired[
        "aws_sdk_iot_wireless.types.event_notification_topic_status.EventNotificationTopicStatus"
    ]
    """<p>Denotes whether the wireless device ID proximity event topic is enabled or disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProximityEventConfiguration) -> dict:
    out: dict = {}
    if "sidewalk" in value:
        import aws_sdk_iot_wireless.types.sidewalk_event_notification_configurations

        out["Sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_event_notification_configurations.serialize_json(
                value["sidewalk"]
            )
        )
    if "wireless_device_id_event_topic" in value:
        import aws_sdk_iot_wireless.types.event_notification_topic_status

        out["WirelessDeviceIdEventTopic"] = (
            aws_sdk_iot_wireless.types.event_notification_topic_status.serialize_json(
                value["wireless_device_id_event_topic"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProximityEventConfiguration:
    out: ProximityEventConfiguration = {}  # type: ignore[typeddict-item]
    if "Sidewalk" in data:
        import aws_sdk_iot_wireless.types.sidewalk_event_notification_configurations

        out["sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_event_notification_configurations.deserialize_json(
                data["Sidewalk"]
            )
        )
    if "WirelessDeviceIdEventTopic" in data:
        import aws_sdk_iot_wireless.types.event_notification_topic_status

        out["wireless_device_id_event_topic"] = (
            aws_sdk_iot_wireless.types.event_notification_topic_status.deserialize_json(
                data["WirelessDeviceIdEventTopic"]
            )
        )
    return out
