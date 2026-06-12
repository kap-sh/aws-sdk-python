"""Generated from Smithy shape ``com.amazonaws.geoplaces#PhonemeTranscriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.phoneme_transcription

PhonemeTranscriptionList: TypeAlias = list[
    "aws_sdk_geo_places.types.phoneme_transcription.PhonemeTranscription"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhonemeTranscriptionList) -> list:
    import aws_sdk_geo_places.types.phoneme_transcription

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_places.types.phoneme_transcription.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhonemeTranscriptionList:
    import aws_sdk_geo_places.types.phoneme_transcription

    out: PhonemeTranscriptionList = []
    for item in data:
        out.append(
            aws_sdk_geo_places.types.phoneme_transcription.deserialize_json(item)
        )
    return out
