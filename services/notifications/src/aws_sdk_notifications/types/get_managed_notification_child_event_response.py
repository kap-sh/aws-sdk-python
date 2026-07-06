"""Generated from Smithy shape ``com.amazonaws.notifications#GetManagedNotificationChildEventResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.creation_time
    import aws_sdk_notifications.types.managed_notification_child_event
    import aws_sdk_notifications.types.managed_notification_child_event_arn
    import aws_sdk_notifications.types.managed_notification_configuration_os_arn


class GetManagedNotificationChildEventResponse(TypedDict, closed=True):
    arn: "aws_sdk_notifications.types.managed_notification_child_event_arn.ManagedNotificationChildEventArn"
    """<p>The ARN of the resource.</p>"""
    managed_notification_configuration_arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> associated with the <code>ManagedNotificationChildEvent</code>.</p>"""
    creation_time: "aws_sdk_notifications.types.creation_time.CreationTime"
    """<p>The creation time of the <code>ManagedNotificationChildEvent</code>.</p>"""
    content: "aws_sdk_notifications.types.managed_notification_child_event.ManagedNotificationChildEvent"
    """<p>The content of the <code>ManagedNotificationChildEvent</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedNotificationChildEventResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["managedNotificationConfigurationArn"] = value[
        "managed_notification_configuration_arn"
    ]
    import aws_sdk_notifications.types.creation_time

    out["creationTime"] = aws_sdk_notifications.types.creation_time.serialize_json(
        value["creation_time"]
    )
    import aws_sdk_notifications.types.managed_notification_child_event

    out["content"] = (
        aws_sdk_notifications.types.managed_notification_child_event.serialize_json(
            value["content"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetManagedNotificationChildEventResponse:
    out: GetManagedNotificationChildEventResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError(
            "GetManagedNotificationChildEventResponse.arn required"
        )
    if "managedNotificationConfigurationArn" in data:
        out["managed_notification_configuration_arn"] = data[
            "managedNotificationConfigurationArn"
        ]
    else:
        raise DeserializationError(
            "GetManagedNotificationChildEventResponse.managed_notification_configuration_arn required"
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
            "GetManagedNotificationChildEventResponse.creation_time required"
        )
    if "content" in data:
        import aws_sdk_notifications.types.managed_notification_child_event

        out["content"] = (
            aws_sdk_notifications.types.managed_notification_child_event.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError(
            "GetManagedNotificationChildEventResponse.content required"
        )
    return out
