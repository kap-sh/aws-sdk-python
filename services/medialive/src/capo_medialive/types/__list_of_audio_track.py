"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfAudioTrack``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.audio_track

__listOfAudioTrack: TypeAlias = list["capo_medialive.types.audio_track.AudioTrack"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAudioTrack) -> list:
    import capo_medialive.types.audio_track

    out: list = []
    for item in value:
        out.append(capo_medialive.types.audio_track.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAudioTrack:
    import capo_medialive.types.audio_track

    out: __listOfAudioTrack = []
    for item in data:
        out.append(capo_medialive.types.audio_track.deserialize_json(item))
    return out
