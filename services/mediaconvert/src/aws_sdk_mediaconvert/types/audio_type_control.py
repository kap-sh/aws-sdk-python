"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioTypeControl``."""

from typing import Literal, TypeAlias, cast

"""When set to FOLLOW_INPUT, if the input contains an ISO 639 audio_type, then that value is passed through to the output. If the input contains no ISO 639 audio_type, the value in Audio Type is included in the output. Otherwise the value in Audio Type is included in the output. Note that this field and audioType are both ignored if audioDescriptionBroadcasterMix is set to BROADCASTER_MIXED_AD."""
AudioTypeControl: TypeAlias = Literal[
    "FOLLOW_INPUT",
    "USE_CONFIGURED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioTypeControl) -> str:
    return value


def deserialize_json(data: str) -> AudioTypeControl:
    return cast(AudioTypeControl, data)
