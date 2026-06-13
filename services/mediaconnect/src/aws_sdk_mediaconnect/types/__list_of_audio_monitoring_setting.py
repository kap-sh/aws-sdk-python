"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfAudioMonitoringSetting``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.audio_monitoring_setting

__listOfAudioMonitoringSetting: TypeAlias = list[
    "aws_sdk_mediaconnect.types.audio_monitoring_setting.AudioMonitoringSetting"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAudioMonitoringSetting) -> list:
    import aws_sdk_mediaconnect.types.audio_monitoring_setting

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.audio_monitoring_setting.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfAudioMonitoringSetting:
    import aws_sdk_mediaconnect.types.audio_monitoring_setting

    out: __listOfAudioMonitoringSetting = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.audio_monitoring_setting.deserialize_json(item)
        )
    return out
