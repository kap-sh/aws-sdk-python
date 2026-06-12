"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetNotificationConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.destination_name
    import aws_sdk_iot_managed_integrations.types.event_type
    import aws_sdk_iot_managed_integrations.types.notification_configuration_created_at
    import aws_sdk_iot_managed_integrations.types.notification_configuration_updated_at
    import aws_sdk_iot_managed_integrations.types.tags_map


class GetNotificationConfigurationResponse(TypedDict):
    event_type: NotRequired[
        "aws_sdk_iot_managed_integrations.types.event_type.EventType"
    ]
    """<p>The type of event triggering a device notification to the customer-managed destination.</p>"""
    destination_name: NotRequired[
        "aws_sdk_iot_managed_integrations.types.destination_name.DestinationName"
    ]
    """<p>The name of the destination for the notification configuration.</p>"""
    created_at: NotRequired[
        "aws_sdk_iot_managed_integrations.types.notification_configuration_created_at.NotificationConfigurationCreatedAt"
    ]
    """<p>The timestamp value of when the notification configuration was created.</p>"""
    updated_at: NotRequired[
        "aws_sdk_iot_managed_integrations.types.notification_configuration_updated_at.NotificationConfigurationUpdatedAt"
    ]
    """<p>The timestamp value of when the notification configuration was last updated.</p>"""
    tags: NotRequired["aws_sdk_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the notification configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotificationConfigurationResponse) -> dict:
    out: dict = {}
    if "event_type" in value:
        import aws_sdk_iot_managed_integrations.types.event_type

        out["EventType"] = (
            aws_sdk_iot_managed_integrations.types.event_type.serialize_json(
                value["event_type"]
            )
        )
    if "destination_name" in value:
        out["DestinationName"] = value["destination_name"]
    if "created_at" in value:
        import aws_sdk_iot_managed_integrations.types.notification_configuration_created_at

        out["CreatedAt"] = (
            aws_sdk_iot_managed_integrations.types.notification_configuration_created_at.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_iot_managed_integrations.types.notification_configuration_updated_at

        out["UpdatedAt"] = (
            aws_sdk_iot_managed_integrations.types.notification_configuration_updated_at.serialize_json(
                value["updated_at"]
            )
        )
    if "tags" in value:
        import aws_sdk_iot_managed_integrations.types.tags_map

        out["Tags"] = aws_sdk_iot_managed_integrations.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetNotificationConfigurationResponse:
    out: GetNotificationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "EventType" in data:
        import aws_sdk_iot_managed_integrations.types.event_type

        out["event_type"] = (
            aws_sdk_iot_managed_integrations.types.event_type.deserialize_json(
                data["EventType"]
            )
        )
    if "DestinationName" in data:
        out["destination_name"] = data["DestinationName"]
    if "CreatedAt" in data:
        import aws_sdk_iot_managed_integrations.types.notification_configuration_created_at

        out["created_at"] = (
            aws_sdk_iot_managed_integrations.types.notification_configuration_created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "UpdatedAt" in data:
        import aws_sdk_iot_managed_integrations.types.notification_configuration_updated_at

        out["updated_at"] = (
            aws_sdk_iot_managed_integrations.types.notification_configuration_updated_at.deserialize_json(
                data["UpdatedAt"]
            )
        )
    if "Tags" in data:
        import aws_sdk_iot_managed_integrations.types.tags_map

        out["tags"] = aws_sdk_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    return out
