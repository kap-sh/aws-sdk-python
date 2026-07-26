"""Generated from Smithy shape ``com.amazonaws.polly#VoiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_polly.types.voice

VoiceList: TypeAlias = list["capo_polly.types.voice.Voice"]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceList) -> list:
    import capo_polly.types.voice

    out: list = []
    for item in value:
        out.append(capo_polly.types.voice.serialize_json(item))
    return out


def deserialize_json(data: list) -> VoiceList:
    import capo_polly.types.voice

    out: VoiceList = []
    for item in data:
        out.append(capo_polly.types.voice.deserialize_json(item))
    return out
