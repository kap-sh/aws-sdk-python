"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfAudioSelector``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.audio_selector

__listOfAudioSelector: TypeAlias = list[
    "aws_sdk_medialive.types.audio_selector.AudioSelector"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAudioSelector) -> list:
    import aws_sdk_medialive.types.audio_selector

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.audio_selector.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAudioSelector:
    import aws_sdk_medialive.types.audio_selector

    out: __listOfAudioSelector = []
    for item in data:
        out.append(aws_sdk_medialive.types.audio_selector.deserialize_json(item))
    return out
