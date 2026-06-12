"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#VoiceProfileSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.voice_profile_summary

VoiceProfileSummaryList: TypeAlias = list[
    "aws_sdk_chime_sdk_voice.types.voice_profile_summary.VoiceProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceProfileSummaryList) -> list:
    import aws_sdk_chime_sdk_voice.types.voice_profile_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_voice.types.voice_profile_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> VoiceProfileSummaryList:
    import aws_sdk_chime_sdk_voice.types.voice_profile_summary

    out: VoiceProfileSummaryList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_voice.types.voice_profile_summary.deserialize_json(item)
        )
    return out
