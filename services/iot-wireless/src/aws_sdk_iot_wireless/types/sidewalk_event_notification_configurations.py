"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkEventNotificationConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.event_notification_topic_status


class SidewalkEventNotificationConfigurations(TypedDict, closed=True):
    amazon_id_event_topic: NotRequired[
        "aws_sdk_iot_wireless.types.event_notification_topic_status.EventNotificationTopicStatus"
    ]
    """<p>Denotes whether the Amazon ID event topic is enabled or disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkEventNotificationConfigurations) -> dict:
    out: dict = {}
    if "amazon_id_event_topic" in value:
        import aws_sdk_iot_wireless.types.event_notification_topic_status

        out["AmazonIdEventTopic"] = (
            aws_sdk_iot_wireless.types.event_notification_topic_status.serialize_json(
                value["amazon_id_event_topic"]
            )
        )
    return out


def deserialize_json(data: dict) -> SidewalkEventNotificationConfigurations:
    out: SidewalkEventNotificationConfigurations = {}  # type: ignore[typeddict-item]
    if "AmazonIdEventTopic" in data:
        import aws_sdk_iot_wireless.types.event_notification_topic_status

        out["amazon_id_event_topic"] = (
            aws_sdk_iot_wireless.types.event_notification_topic_status.deserialize_json(
                data["AmazonIdEventTopic"]
            )
        )
    return out
