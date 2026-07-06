"""Generated from Smithy shape ``com.amazonaws.notifications#ListManagedNotificationChannelAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_notifications.types.managed_notification_configuration_os_arn
    import aws_sdk_notifications.types.next_token


class ListManagedNotificationChannelAssociationsRequest(TypedDict, closed=True):
    managed_notification_configuration_arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to match.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to be returned in this call. Defaults to 20.</p>"""
    next_token: NotRequired["aws_sdk_notifications.types.next_token.NextToken"]
    """<p>The start token for paginated calls. Retrieved from the response of a previous <code>ListManagedNotificationChannelAssociations</code> call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedNotificationChannelAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListManagedNotificationChannelAssociationsRequest:
    out: ListManagedNotificationChannelAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
