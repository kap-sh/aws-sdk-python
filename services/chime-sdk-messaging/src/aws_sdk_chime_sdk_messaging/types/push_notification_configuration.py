"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#PushNotificationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.push_notification_body
    import aws_sdk_chime_sdk_messaging.types.push_notification_title
    import aws_sdk_chime_sdk_messaging.types.push_notification_type


class PushNotificationConfiguration(TypedDict, closed=True):
    title: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.push_notification_title.PushNotificationTitle"
    ]
    """<p>The title of the push notification.</p>"""
    body: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.push_notification_body.PushNotificationBody"
    ]
    """<p>The body of the push notification.</p>"""
    type: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.push_notification_type.PushNotificationType"
    ]
    """<p>Enum value that indicates the type of the push notification for a message. <code>DEFAULT</code>: Normal mobile push notification. <code>VOIP</code>: VOIP mobile push notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PushNotificationConfiguration) -> dict:
    out: dict = {}
    if "title" in value:
        out["Title"] = value["title"]
    if "body" in value:
        out["Body"] = value["body"]
    if "type" in value:
        import aws_sdk_chime_sdk_messaging.types.push_notification_type

        out["Type"] = (
            aws_sdk_chime_sdk_messaging.types.push_notification_type.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> PushNotificationConfiguration:
    out: PushNotificationConfiguration = {}  # type: ignore[typeddict-item]
    if "Title" in data:
        out["title"] = data["Title"]
    if "Body" in data:
        out["body"] = data["Body"]
    if "Type" in data:
        import aws_sdk_chime_sdk_messaging.types.push_notification_type

        out["type"] = (
            aws_sdk_chime_sdk_messaging.types.push_notification_type.deserialize_json(
                data["Type"]
            )
        )
    return out
