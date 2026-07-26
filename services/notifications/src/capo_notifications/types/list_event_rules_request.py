"""Generated from Smithy shape ``com.amazonaws.notifications#ListEventRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.next_token
    import capo_notifications.types.notification_configuration_arn


class ListEventRulesRequest(TypedDict, closed=True):
    notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the <code>NotificationConfiguration</code>.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to be returned in this call. The default value is 20.</p>"""
    next_token: NotRequired["capo_notifications.types.next_token.NextToken"]
    """<p>The start token for paginated calls. Retrieved from the response of a previous <code>ListEventRules</code> call. Next token uses Base64 encoding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventRulesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEventRulesRequest:
    out: ListEventRulesRequest = {}  # type: ignore[typeddict-item]
    return out
