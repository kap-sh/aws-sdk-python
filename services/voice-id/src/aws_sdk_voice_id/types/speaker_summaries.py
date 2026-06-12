"""Generated from Smithy shape ``com.amazonaws.voiceid#SpeakerSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.speaker_summary

SpeakerSummaries: TypeAlias = list[
    "aws_sdk_voice_id.types.speaker_summary.SpeakerSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SpeakerSummaries) -> list:
    import aws_sdk_voice_id.types.speaker_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_voice_id.types.speaker_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> SpeakerSummaries:
    import aws_sdk_voice_id.types.speaker_summary

    out: SpeakerSummaries = []
    for item in data:
        out.append(
            aws_sdk_voice_id.types.speaker_summary.deserialize_aws_json_1_0(item)
        )
    return out
