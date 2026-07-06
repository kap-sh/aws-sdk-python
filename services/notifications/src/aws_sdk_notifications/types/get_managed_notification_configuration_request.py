"""Generated from Smithy shape ``com.amazonaws.notifications#GetManagedNotificationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_notifications.types.managed_notification_configuration_os_arn


class GetManagedNotificationConfigurationRequest(TypedDict, closed=True):
    arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedNotificationConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetManagedNotificationConfigurationRequest:
    out: GetManagedNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
