"""Generated from Smithy shape ``com.amazonaws.notifications#GetManagedNotificationChildEventResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notifications.types.creation_time
    import capo_notifications.types.managed_notification_child_event
    import capo_notifications.types.managed_notification_child_event_arn
    import capo_notifications.types.managed_notification_configuration_os_arn


class GetManagedNotificationChildEventResponse(TypedDict, closed=True):
    arn: "capo_notifications.types.managed_notification_child_event_arn.ManagedNotificationChildEventArn"
    """<p>The ARN of the resource.</p>"""
    managed_notification_configuration_arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> associated with the <code>ManagedNotificationChildEvent</code>.</p>"""
    creation_time: "capo_notifications.types.creation_time.CreationTime"
    """<p>The creation time of the <code>ManagedNotificationChildEvent</code>.</p>"""
    content: "capo_notifications.types.managed_notification_child_event.ManagedNotificationChildEvent"
    """<p>The content of the <code>ManagedNotificationChildEvent</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedNotificationChildEventResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["managedNotificationConfigurationArn"] = value[
        "managed_notification_configuration_arn"
    ]
    import capo_notifications.types.creation_time

    out["creationTime"] = capo_notifications.types.creation_time.serialize_json(
        value["creation_time"]
    )
    import capo_notifications.types.managed_notification_child_event

    out["content"] = (
        capo_notifications.types.managed_notification_child_event.serialize_json(
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
        import capo_notifications.types.creation_time

        out["creation_time"] = capo_notifications.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "GetManagedNotificationChildEventResponse.creation_time required"
        )
    if "content" in data:
        import capo_notifications.types.managed_notification_child_event

        out["content"] = (
            capo_notifications.types.managed_notification_child_event.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError(
            "GetManagedNotificationChildEventResponse.content required"
        )
    return out
