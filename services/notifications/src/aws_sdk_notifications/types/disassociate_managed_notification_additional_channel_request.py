"""Generated from Smithy shape ``com.amazonaws.notifications#DisassociateManagedNotificationAdditionalChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.channel_arn
    import aws_sdk_notifications.types.managed_notification_configuration_os_arn


class DisassociateManagedNotificationAdditionalChannelRequest(TypedDict, closed=True):
    channel_arn: "aws_sdk_notifications.types.channel_arn.ChannelArn"
    """<p>The Amazon Resource Name (ARN) of the Channel to associate with the <code>ManagedNotificationConfiguration</code>.</p>"""
    managed_notification_configuration_arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn"
    """<p>The Amazon Resource Name (ARN) of the Managed Notification Configuration to associate with the additional Channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: DisassociateManagedNotificationAdditionalChannelRequest,
) -> dict:
    out: dict = {}
    out["managedNotificationConfigurationArn"] = value[
        "managed_notification_configuration_arn"
    ]
    return out


def deserialize_json(
    data: dict,
) -> DisassociateManagedNotificationAdditionalChannelRequest:
    out: DisassociateManagedNotificationAdditionalChannelRequest = {}  # type: ignore[typeddict-item]
    if "managedNotificationConfigurationArn" in data:
        out["managed_notification_configuration_arn"] = data[
            "managedNotificationConfigurationArn"
        ]
    else:
        raise DeserializationError(
            "DisassociateManagedNotificationAdditionalChannelRequest.managed_notification_configuration_arn required"
        )
    return out
