"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkResourceTypeEventConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.event_notification_topic_status


class SidewalkResourceTypeEventConfiguration(TypedDict):
    wireless_device_event_topic: NotRequired[
        "aws_sdk_iot_wireless.types.event_notification_topic_status.EventNotificationTopicStatus"
    ]
    """<p>Denotes whether the wireless device join event topic is enabled or disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkResourceTypeEventConfiguration) -> dict:
    out: dict = {}
    if "wireless_device_event_topic" in value:
        import aws_sdk_iot_wireless.types.event_notification_topic_status

        out["WirelessDeviceEventTopic"] = (
            aws_sdk_iot_wireless.types.event_notification_topic_status.serialize_json(
                value["wireless_device_event_topic"]
            )
        )
    return out


def deserialize_json(data: dict) -> SidewalkResourceTypeEventConfiguration:
    out: SidewalkResourceTypeEventConfiguration = {}  # type: ignore[typeddict-item]
    if "WirelessDeviceEventTopic" in data:
        import aws_sdk_iot_wireless.types.event_notification_topic_status

        out["wireless_device_event_topic"] = (
            aws_sdk_iot_wireless.types.event_notification_topic_status.deserialize_json(
                data["WirelessDeviceEventTopic"]
            )
        )
    return out
