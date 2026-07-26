"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#StreamingNotificationTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.streaming_notification_target

StreamingNotificationTargetList: TypeAlias = list[
    "capo_chime_sdk_voice.types.streaming_notification_target.StreamingNotificationTarget"
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamingNotificationTargetList) -> list:
    import capo_chime_sdk_voice.types.streaming_notification_target

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_voice.types.streaming_notification_target.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StreamingNotificationTargetList:
    import capo_chime_sdk_voice.types.streaming_notification_target

    out: StreamingNotificationTargetList = []
    for item in data:
        out.append(
            capo_chime_sdk_voice.types.streaming_notification_target.deserialize_json(
                item
            )
        )
    return out
