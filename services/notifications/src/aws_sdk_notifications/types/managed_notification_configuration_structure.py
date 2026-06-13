"""Generated from Smithy shape ``com.amazonaws.notifications#ManagedNotificationConfigurationStructure``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.managed_notification_configuration_description
    import aws_sdk_notifications.types.managed_notification_configuration_name
    import aws_sdk_notifications.types.managed_notification_configuration_os_arn


class ManagedNotificationConfigurationStructure(TypedDict):
    arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code>.</p>"""
    name: "aws_sdk_notifications.types.managed_notification_configuration_name.ManagedNotificationConfigurationName"
    """<p>The name of the <code>ManagedNotificationConfiguration</code>.</p>"""
    description: "aws_sdk_notifications.types.managed_notification_configuration_description.ManagedNotificationConfigurationDescription"
    """<p>The description of the <code>ManagedNotificationConfiguration</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedNotificationConfigurationStructure) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ManagedNotificationConfigurationStructure:
    out: ManagedNotificationConfigurationStructure = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError(
            "ManagedNotificationConfigurationStructure.arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "ManagedNotificationConfigurationStructure.name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError(
            "ManagedNotificationConfigurationStructure.description required"
        )
    return out
