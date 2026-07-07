"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#StreamingNotificationTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.notification_target


class StreamingNotificationTarget(TypedDict, closed=True):
    notification_target: NotRequired[
        "aws_sdk_chime_sdk_voice.types.notification_target.NotificationTarget"
    ]
    """<p>The streaming notification target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamingNotificationTarget) -> dict:
    out: dict = {}
    if "notification_target" in value:
        import aws_sdk_chime_sdk_voice.types.notification_target

        out["NotificationTarget"] = (
            aws_sdk_chime_sdk_voice.types.notification_target.serialize_json(
                value["notification_target"]
            )
        )
    return out


def deserialize_json(data: dict) -> StreamingNotificationTarget:
    out: StreamingNotificationTarget = {}  # type: ignore[typeddict-item]
    if "NotificationTarget" in data:
        import aws_sdk_chime_sdk_voice.types.notification_target

        out["notification_target"] = (
            aws_sdk_chime_sdk_voice.types.notification_target.deserialize_json(
                data["NotificationTarget"]
            )
        )
    return out
