"""Generated from Smithy shape ``com.amazonaws.notifications#GetManagedNotificationChildEventRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_notifications.types.locale_code
    import aws_sdk_notifications.types.managed_notification_child_event_arn

class GetManagedNotificationChildEventRequest(TypedDict):
    arn: "aws_sdk_notifications.types.managed_notification_child_event_arn.ManagedNotificationChildEventArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationChildEvent</code> to return.</p>"""
    locale: NotRequired["aws_sdk_notifications.types.locale_code.LocaleCode"]
    """<p>The locale code of the language used for the retrieved <code>ManagedNotificationChildEvent</code>. The default locale is English <code>en_US</code>.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetManagedNotificationChildEventRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetManagedNotificationChildEventRequest:
    out: GetManagedNotificationChildEventRequest = {}  # type: ignore[typeddict-item]
    return out