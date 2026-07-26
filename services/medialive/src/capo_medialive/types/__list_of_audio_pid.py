"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfAudioPid``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.audio_pid

__listOfAudioPid: TypeAlias = list["capo_medialive.types.audio_pid.AudioPid"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAudioPid) -> list:
    import capo_medialive.types.audio_pid

    out: list = []
    for item in value:
        out.append(capo_medialive.types.audio_pid.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAudioPid:
    import capo_medialive.types.audio_pid

    out: __listOfAudioPid = []
    for item in data:
        out.append(capo_medialive.types.audio_pid.deserialize_json(item))
    return out
