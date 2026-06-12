"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#StreamingNotificationTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.streaming_notification_target

StreamingNotificationTargetList: TypeAlias = list[
    "aws_sdk_chime_sdk_voice.types.streaming_notification_target.StreamingNotificationTarget"
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamingNotificationTargetList) -> list:
    import aws_sdk_chime_sdk_voice.types.streaming_notification_target

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_voice.types.streaming_notification_target.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StreamingNotificationTargetList:
    import aws_sdk_chime_sdk_voice.types.streaming_notification_target

    out: StreamingNotificationTargetList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_voice.types.streaming_notification_target.deserialize_json(
                item
            )
        )
    return out
