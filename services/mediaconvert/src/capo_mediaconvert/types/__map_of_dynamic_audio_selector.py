"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__mapOfDynamicAudioSelector``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.dynamic_audio_selector

__mapOfDynamicAudioSelector: TypeAlias = dict[
    "capo_mediaconvert.types.__string.__string",
    "capo_mediaconvert.types.dynamic_audio_selector.DynamicAudioSelector",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: __mapOfDynamicAudioSelector) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_mediaconvert.types.dynamic_audio_selector

        out[key] = capo_mediaconvert.types.dynamic_audio_selector.serialize_json(value)
    return out


def deserialize_json(data: dict) -> __mapOfDynamicAudioSelector:
    out: __mapOfDynamicAudioSelector = {}
    for key, value in data.items():
        import capo_mediaconvert.types.dynamic_audio_selector

        out[key] = capo_mediaconvert.types.dynamic_audio_selector.deserialize_json(
            value
        )
    return out
