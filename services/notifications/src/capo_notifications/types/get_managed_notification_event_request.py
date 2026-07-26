"""Generated from Smithy shape ``com.amazonaws.notifications#GetManagedNotificationEventRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.locale_code
    import capo_notifications.types.managed_notification_event_arn


class GetManagedNotificationEventRequest(TypedDict, closed=True):
    arn: "capo_notifications.types.managed_notification_event_arn.ManagedNotificationEventArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationEvent</code> to return.</p>"""
    locale: NotRequired["capo_notifications.types.locale_code.LocaleCode"]
    """<p>The locale code of the language used for the retrieved <code>ManagedNotificationEvent</code>. The default locale is English <code>(en_US)</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedNotificationEventRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetManagedNotificationEventRequest:
    out: GetManagedNotificationEventRequest = {}  # type: ignore[typeddict-item]
    return out
