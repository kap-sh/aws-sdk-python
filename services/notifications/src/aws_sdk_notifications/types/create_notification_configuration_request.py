"""Generated from Smithy shape ``com.amazonaws.notifications#CreateNotificationConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.aggregation_duration
    import aws_sdk_notifications.types.notification_configuration_description
    import aws_sdk_notifications.types.notification_configuration_name
    import aws_sdk_notifications.types.tag_map


class CreateNotificationConfigurationRequest(TypedDict):
    name: "aws_sdk_notifications.types.notification_configuration_name.NotificationConfigurationName"
    """<p>The name of the <code>NotificationConfiguration</code>. Supports RFC 3986's unreserved characters.</p>"""
    description: "aws_sdk_notifications.types.notification_configuration_description.NotificationConfigurationDescription"
    """<p>The description of the <code>NotificationConfiguration</code>.</p>"""
    aggregation_duration: NotRequired[
        "aws_sdk_notifications.types.aggregation_duration.AggregationDuration"
    ]
    """<p>The aggregation preference of the <code>NotificationConfiguration</code>.</p> <ul> <li> <p>Values:</p> <ul> <li> <p> <code>LONG</code> </p> <ul> <li> <p>Aggregate notifications for long periods of time (12 hours).</p> </li> </ul> </li> <li> <p> <code>SHORT</code> </p> <ul> <li> <p>Aggregate notifications for short periods of time (5 minutes).</p> </li> </ul> </li> <li> <p> <code>NONE</code> </p> <ul> <li> <p>Don't aggregate notifications.</p> </li> </ul> </li> </ul> </li> </ul>"""
    tags: NotRequired["aws_sdk_notifications.types.tag_map.TagMap"]
    """<p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNotificationConfigurationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["description"] = value["description"]
    if "aggregation_duration" in value:
        out["aggregationDuration"] = value["aggregation_duration"]
    if "tags" in value:
        import aws_sdk_notifications.types.tag_map

        out["tags"] = aws_sdk_notifications.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateNotificationConfigurationRequest:
    out: CreateNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CreateNotificationConfigurationRequest.name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError(
            "CreateNotificationConfigurationRequest.description required"
        )
    if "aggregationDuration" in data:
        out["aggregation_duration"] = data["aggregationDuration"]
    if "tags" in data:
        import aws_sdk_notifications.types.tag_map

        out["tags"] = aws_sdk_notifications.types.tag_map.deserialize_json(data["tags"])
    return out
