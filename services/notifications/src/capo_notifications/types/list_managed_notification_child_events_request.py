"""Generated from Smithy shape ``com.amazonaws.notifications#ListManagedNotificationChildEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_notifications.types.account_id
    import capo_notifications.types.locale_code
    import capo_notifications.types.managed_notification_event_arn
    import capo_notifications.types.next_token
    import capo_notifications.types.organizational_unit_id


class ListManagedNotificationChildEventsRequest(TypedDict, closed=True):
    aggregate_managed_notification_event_arn: "capo_notifications.types.managed_notification_event_arn.ManagedNotificationEventArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationEvent</code>.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The earliest time of events to return from this call.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>Latest time of events to return from this call.</p>"""
    locale: NotRequired["capo_notifications.types.locale_code.LocaleCode"]
    """<p>The locale code of the language used for the retrieved <code>NotificationEvent</code>. The default locale is English.<code>en_US</code>.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to be returned in this call. Defaults to 20.</p>"""
    related_account: NotRequired["capo_notifications.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID associated with the Managed Notification Child Events.</p>"""
    organizational_unit_id: NotRequired[
        "capo_notifications.types.organizational_unit_id.OrganizationalUnitId"
    ]
    """<p>The identifier of the Amazon Web Services Organizations organizational unit (OU) associated with the Managed Notification Child Events.</p>"""
    next_token: NotRequired["capo_notifications.types.next_token.NextToken"]
    """<p>The start token for paginated calls. Retrieved from the response of a previous ListManagedNotificationChannelAssociations call. Next token uses Base64 encoding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedNotificationChildEventsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListManagedNotificationChildEventsRequest:
    out: ListManagedNotificationChildEventsRequest = {}  # type: ignore[typeddict-item]
    return out
