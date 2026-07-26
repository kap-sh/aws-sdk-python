"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfAudioFeedInput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.audio_feed_input

__listOfAudioFeedInput: TypeAlias = list[
    "capo_medialive.types.audio_feed_input.AudioFeedInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAudioFeedInput) -> list:
    import capo_medialive.types.audio_feed_input

    out: list = []
    for item in value:
        out.append(capo_medialive.types.audio_feed_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAudioFeedInput:
    import capo_medialive.types.audio_feed_input

    out: __listOfAudioFeedInput = []
    for item in data:
        out.append(capo_medialive.types.audio_feed_input.deserialize_json(item))
    return out
