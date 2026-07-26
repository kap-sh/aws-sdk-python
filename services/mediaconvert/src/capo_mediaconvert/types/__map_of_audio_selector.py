"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__mapOfAudioSelector``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.audio_selector

__mapOfAudioSelector: TypeAlias = dict[
    "capo_mediaconvert.types.__string.__string",
    "capo_mediaconvert.types.audio_selector.AudioSelector",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: __mapOfAudioSelector) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_mediaconvert.types.audio_selector

        out[key] = capo_mediaconvert.types.audio_selector.serialize_json(value)
    return out


def deserialize_json(data: dict) -> __mapOfAudioSelector:
    out: __mapOfAudioSelector = {}
    for key, value in data.items():
        import capo_mediaconvert.types.audio_selector

        out[key] = capo_mediaconvert.types.audio_selector.deserialize_json(value)
    return out
