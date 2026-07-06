"""Generated from Smithy shape ``com.amazonaws.notifications#ListManagedNotificationConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_notifications.types.channel_identifier
    import aws_sdk_notifications.types.next_token


class ListManagedNotificationConfigurationsRequest(TypedDict, closed=True):
    channel_identifier: NotRequired[
        "aws_sdk_notifications.types.channel_identifier.ChannelIdentifier"
    ]
    """<p>The identifier or ARN of the notification channel to filter configurations by.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to be returned in this call. Defaults to 20.</p>"""
    next_token: NotRequired["aws_sdk_notifications.types.next_token.NextToken"]
    """<p>The start token for paginated calls. Retrieved from the response of a previous ListManagedNotificationChannelAssociations call. Next token uses Base64 encoding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedNotificationConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListManagedNotificationConfigurationsRequest:
    out: ListManagedNotificationConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
