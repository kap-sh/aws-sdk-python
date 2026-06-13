"""Generated from Smithy shape ``com.amazonaws.notifications#GetNotificationEventRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_notifications.types.locale_code
    import aws_sdk_notifications.types.notification_event_arn


class GetNotificationEventRequest(TypedDict):
    arn: "aws_sdk_notifications.types.notification_event_arn.NotificationEventArn"
    """<p>The Amazon Resource Name (ARN) of the <code>NotificationEvent</code> to return.</p>"""
    locale: NotRequired["aws_sdk_notifications.types.locale_code.LocaleCode"]
    """<p>The locale code of the language used for the retrieved <code>NotificationEvent</code>. The default locale is English <code>en_US</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotificationEventRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNotificationEventRequest:
    out: GetNotificationEventRequest = {}  # type: ignore[typeddict-item]
    return out
