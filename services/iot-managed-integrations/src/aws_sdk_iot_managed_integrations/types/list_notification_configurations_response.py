"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListNotificationConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.next_token
    import aws_sdk_iot_managed_integrations.types.notification_configuration_list_definition


class ListNotificationConfigurationsResponse(TypedDict):
    notification_configuration_list: NotRequired[
        "aws_sdk_iot_managed_integrations.types.notification_configuration_list_definition.NotificationConfigurationListDefinition"
    ]
    """<p>The list of notification configurations.</p>"""
    next_token: NotRequired[
        "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
    ]
    """<p>A token that can be used to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationConfigurationsResponse) -> dict:
    out: dict = {}
    if "notification_configuration_list" in value:
        import aws_sdk_iot_managed_integrations.types.notification_configuration_list_definition

        out["NotificationConfigurationList"] = (
            aws_sdk_iot_managed_integrations.types.notification_configuration_list_definition.serialize_json(
                value["notification_configuration_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNotificationConfigurationsResponse:
    out: ListNotificationConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "NotificationConfigurationList" in data:
        import aws_sdk_iot_managed_integrations.types.notification_configuration_list_definition

        out["notification_configuration_list"] = (
            aws_sdk_iot_managed_integrations.types.notification_configuration_list_definition.deserialize_json(
                data["NotificationConfigurationList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
