"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__mapOfAudioSelectorGroup``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.audio_selector_group

__mapOfAudioSelectorGroup: TypeAlias = dict[
    "capo_mediaconvert.types.__string.__string",
    "capo_mediaconvert.types.audio_selector_group.AudioSelectorGroup",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: __mapOfAudioSelectorGroup) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_mediaconvert.types.audio_selector_group

        out[key] = capo_mediaconvert.types.audio_selector_group.serialize_json(value)
    return out


def deserialize_json(data: dict) -> __mapOfAudioSelectorGroup:
    out: __mapOfAudioSelectorGroup = {}
    for key, value in data.items():
        import capo_mediaconvert.types.audio_selector_group

        out[key] = capo_mediaconvert.types.audio_selector_group.deserialize_json(value)
    return out
