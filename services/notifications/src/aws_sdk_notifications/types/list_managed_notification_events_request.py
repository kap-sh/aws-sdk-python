"""Generated from Smithy shape ``com.amazonaws.notifications#ListManagedNotificationEventsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_notifications.types.account_id
    import aws_sdk_notifications.types.locale_code
    import aws_sdk_notifications.types.next_token
    import aws_sdk_notifications.types.organizational_unit_id
    import aws_sdk_notifications.types.source


class ListManagedNotificationEventsRequest(TypedDict):
    start_time: NotRequired["datetime.datetime"]
    """<p>The earliest time of events to return from this call.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>Latest time of events to return from this call.</p>"""
    locale: NotRequired["aws_sdk_notifications.types.locale_code.LocaleCode"]
    """<p>The locale code of the language used for the retrieved NotificationEvent. The default locale is English (en_US).</p>"""
    source: NotRequired["aws_sdk_notifications.types.source.Source"]
    """<p>The Amazon Web Services service the event originates from. For example aws.cloudwatch.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to be returned in this call. Defaults to 20.</p>"""
    next_token: NotRequired["aws_sdk_notifications.types.next_token.NextToken"]
    """<p>The start token for paginated calls. Retrieved from the response of a previous <code>ListManagedNotificationChannelAssociations</code> call. Next token uses Base64 encoding.</p>"""
    organizational_unit_id: NotRequired[
        "aws_sdk_notifications.types.organizational_unit_id.OrganizationalUnitId"
    ]
    """<p>The Organizational Unit Id that an Amazon Web Services account belongs to.</p>"""
    related_account: NotRequired["aws_sdk_notifications.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID associated with the Managed Notification Events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedNotificationEventsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListManagedNotificationEventsRequest:
    out: ListManagedNotificationEventsRequest = {}  # type: ignore[typeddict-item]
    return out
