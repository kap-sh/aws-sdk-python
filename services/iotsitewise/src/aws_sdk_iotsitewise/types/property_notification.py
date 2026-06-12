"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PropertyNotification``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.property_notification_state
    import aws_sdk_iotsitewise.types.property_notification_topic


class PropertyNotification(TypedDict):
    topic: "aws_sdk_iotsitewise.types.property_notification_topic.PropertyNotificationTopic"
    """<p>The MQTT topic to which IoT SiteWise publishes property value update notifications.</p>"""
    state: "aws_sdk_iotsitewise.types.property_notification_state.PropertyNotificationState"
    """<p>The current notification state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyNotification) -> dict:
    out: dict = {}
    out["topic"] = value["topic"]
    import aws_sdk_iotsitewise.types.property_notification_state

    out["state"] = aws_sdk_iotsitewise.types.property_notification_state.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> PropertyNotification:
    out: PropertyNotification = {}  # type: ignore[typeddict-item]
    if "topic" in data:
        out["topic"] = data["topic"]
    else:
        raise DeserializationError("PropertyNotification.topic required")
    if "state" in data:
        import aws_sdk_iotsitewise.types.property_notification_state

        out["state"] = (
            aws_sdk_iotsitewise.types.property_notification_state.deserialize_json(
                data["state"]
            )
        )
    else:
        raise DeserializationError("PropertyNotification.state required")
    return out
