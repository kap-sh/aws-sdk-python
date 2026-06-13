"""Generated from Smithy shape ``com.amazonaws.notifications#AssociateChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.channel_arn
    import aws_sdk_notifications.types.notification_configuration_arn


class AssociateChannelRequest(TypedDict):
    arn: "aws_sdk_notifications.types.channel_arn.ChannelArn"
    """<p>The Amazon Resource Name (ARN) of the Channel to associate with the <code>NotificationConfiguration</code>.</p> <p>Supported ARNs include Amazon Q Developer in chat applications, the Console Mobile Application, and notifications-contacts.</p>"""
    notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The ARN of the <code>NotificationConfiguration</code> to associate with the Channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateChannelRequest) -> dict:
    out: dict = {}
    out["notificationConfigurationArn"] = value["notification_configuration_arn"]
    return out


def deserialize_json(data: dict) -> AssociateChannelRequest:
    out: AssociateChannelRequest = {}  # type: ignore[typeddict-item]
    if "notificationConfigurationArn" in data:
        out["notification_configuration_arn"] = data["notificationConfigurationArn"]
    else:
        raise DeserializationError(
            "AssociateChannelRequest.notification_configuration_arn required"
        )
    return out
