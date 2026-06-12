"""Generated from Smithy shape ``com.amazonaws.polly#SpeechMarkTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_polly.types.speech_mark_type

SpeechMarkTypeList: TypeAlias = list[
    "aws_sdk_polly.types.speech_mark_type.SpeechMarkType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SpeechMarkTypeList) -> list:
    import aws_sdk_polly.types.speech_mark_type

    out: list = []
    for item in value:
        out.append(aws_sdk_polly.types.speech_mark_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> SpeechMarkTypeList:
    import aws_sdk_polly.types.speech_mark_type

    out: SpeechMarkTypeList = []
    for item in data:
        out.append(aws_sdk_polly.types.speech_mark_type.deserialize_json(item))
    return out
