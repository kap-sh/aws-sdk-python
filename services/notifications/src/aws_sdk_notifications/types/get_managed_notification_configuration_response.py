"""Generated from Smithy shape ``com.amazonaws.notifications#GetManagedNotificationConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.managed_notification_configuration_description
    import aws_sdk_notifications.types.managed_notification_configuration_name
    import aws_sdk_notifications.types.managed_notification_configuration_os_arn


class GetManagedNotificationConfigurationResponse(TypedDict, closed=True):
    arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn"
    """<p>The ARN of the <code>ManagedNotificationConfiguration</code> resource.</p>"""
    name: "aws_sdk_notifications.types.managed_notification_configuration_name.ManagedNotificationConfigurationName"
    """<p>The name of the <code>ManagedNotificationConfiguration</code>.</p>"""
    description: "aws_sdk_notifications.types.managed_notification_configuration_description.ManagedNotificationConfigurationDescription"
    """<p>The description of the <code>ManagedNotificationConfiguration</code>.</p>"""
    category: "str"
    """<p>The category of the <code>ManagedNotificationConfiguration</code>.</p>"""
    sub_category: "str"
    """<p>The subCategory of the <code>ManagedNotificationConfiguration</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedNotificationConfigurationResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    out["category"] = value["category"]
    out["subCategory"] = value["sub_category"]
    return out


def deserialize_json(data: dict) -> GetManagedNotificationConfigurationResponse:
    out: GetManagedNotificationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError(
            "GetManagedNotificationConfigurationResponse.arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "GetManagedNotificationConfigurationResponse.name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError(
            "GetManagedNotificationConfigurationResponse.description required"
        )
    if "category" in data:
        out["category"] = data["category"]
    else:
        raise DeserializationError(
            "GetManagedNotificationConfigurationResponse.category required"
        )
    if "subCategory" in data:
        out["sub_category"] = data["subCategory"]
    else:
        raise DeserializationError(
            "GetManagedNotificationConfigurationResponse.sub_category required"
        )
    return out
