"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SpeakerSearchResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.speaker_search_result

SpeakerSearchResultList: TypeAlias = list[
    "aws_sdk_chime_sdk_voice.types.speaker_search_result.SpeakerSearchResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: SpeakerSearchResultList) -> list:
    import aws_sdk_chime_sdk_voice.types.speaker_search_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_voice.types.speaker_search_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SpeakerSearchResultList:
    import aws_sdk_chime_sdk_voice.types.speaker_search_result

    out: SpeakerSearchResultList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_voice.types.speaker_search_result.deserialize_json(item)
        )
    return out
