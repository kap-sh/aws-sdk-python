"""Generated from Smithy shape ``com.amazonaws.notifications#GetNotificationEventResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.creation_time
    import aws_sdk_notifications.types.notification_configuration_arn
    import aws_sdk_notifications.types.notification_event_arn
    import aws_sdk_notifications.types.notification_event_schema


class GetNotificationEventResponse(TypedDict):
    arn: "aws_sdk_notifications.types.notification_event_arn.NotificationEventArn"
    """<p>The ARN of the resource.</p>"""
    notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The ARN of the <code>NotificationConfiguration</code>.</p>"""
    creation_time: "aws_sdk_notifications.types.creation_time.CreationTime"
    """<p>The creation time of the <code>NotificationEvent</code>.</p>"""
    content: (
        "aws_sdk_notifications.types.notification_event_schema.NotificationEventSchema"
    )
    """<p>The content of the <code>NotificationEvent</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotificationEventResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["notificationConfigurationArn"] = value["notification_configuration_arn"]
    import aws_sdk_notifications.types.creation_time

    out["creationTime"] = aws_sdk_notifications.types.creation_time.serialize_json(
        value["creation_time"]
    )
    import aws_sdk_notifications.types.notification_event_schema

    out["content"] = (
        aws_sdk_notifications.types.notification_event_schema.serialize_json(
            value["content"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetNotificationEventResponse:
    out: GetNotificationEventResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetNotificationEventResponse.arn required")
    if "notificationConfigurationArn" in data:
        out["notification_configuration_arn"] = data["notificationConfigurationArn"]
    else:
        raise DeserializationError(
            "GetNotificationEventResponse.notification_configuration_arn required"
        )
    if "creationTime" in data:
        import aws_sdk_notifications.types.creation_time

        out["creation_time"] = (
            aws_sdk_notifications.types.creation_time.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetNotificationEventResponse.creation_time required"
        )
    if "content" in data:
        import aws_sdk_notifications.types.notification_event_schema

        out["content"] = (
            aws_sdk_notifications.types.notification_event_schema.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("GetNotificationEventResponse.content required")
    return out
