"""Generated from Smithy shape ``com.amazonaws.polly#SpeechMarkTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_polly.types.speech_mark_type

SpeechMarkTypeList: TypeAlias = list["capo_polly.types.speech_mark_type.SpeechMarkType"]


# --- restJson1 ser/de ---
def serialize_json(value: SpeechMarkTypeList) -> list:
    import capo_polly.types.speech_mark_type

    out: list = []
    for item in value:
        out.append(capo_polly.types.speech_mark_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> SpeechMarkTypeList:
    import capo_polly.types.speech_mark_type

    out: SpeechMarkTypeList = []
    for item in data:
        out.append(capo_polly.types.speech_mark_type.deserialize_json(item))
    return out
