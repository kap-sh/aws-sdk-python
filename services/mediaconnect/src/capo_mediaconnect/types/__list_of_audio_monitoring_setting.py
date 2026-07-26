"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfAudioMonitoringSetting``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.audio_monitoring_setting

__listOfAudioMonitoringSetting: TypeAlias = list[
    "capo_mediaconnect.types.audio_monitoring_setting.AudioMonitoringSetting"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAudioMonitoringSetting) -> list:
    import capo_mediaconnect.types.audio_monitoring_setting

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.audio_monitoring_setting.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfAudioMonitoringSetting:
    import capo_mediaconnect.types.audio_monitoring_setting

    out: __listOfAudioMonitoringSetting = []
    for item in data:
        out.append(
            capo_mediaconnect.types.audio_monitoring_setting.deserialize_json(item)
        )
    return out
