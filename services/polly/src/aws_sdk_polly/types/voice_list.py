"""Generated from Smithy shape ``com.amazonaws.polly#VoiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_polly.types.voice

VoiceList: TypeAlias = list["aws_sdk_polly.types.voice.Voice"]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceList) -> list:
    import aws_sdk_polly.types.voice

    out: list = []
    for item in value:
        out.append(aws_sdk_polly.types.voice.serialize_json(item))
    return out


def deserialize_json(data: list) -> VoiceList:
    import aws_sdk_polly.types.voice

    out: VoiceList = []
    for item in data:
        out.append(aws_sdk_polly.types.voice.deserialize_json(item))
    return out
