"""Generated from Smithy shape ``com.amazonaws.notifications#ListChannelsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_notifications.types.next_token
    import aws_sdk_notifications.types.notification_configuration_arn


class ListChannelsRequest(TypedDict):
    notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code>.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to be returned in this call. The default value is 20.</p>"""
    next_token: NotRequired["aws_sdk_notifications.types.next_token.NextToken"]
    """<p>The start token for paginated calls. Retrieved from the response of a previous ListNotificationEvents call. <code>NextToken</code> uses Base64 encoding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListChannelsRequest:
    out: ListChannelsRequest = {}  # type: ignore[typeddict-item]
    return out
