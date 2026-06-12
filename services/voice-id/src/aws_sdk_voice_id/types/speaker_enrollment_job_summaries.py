"""Generated from Smithy shape ``com.amazonaws.voiceid#SpeakerEnrollmentJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.speaker_enrollment_job_summary

SpeakerEnrollmentJobSummaries: TypeAlias = list[
    "aws_sdk_voice_id.types.speaker_enrollment_job_summary.SpeakerEnrollmentJobSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SpeakerEnrollmentJobSummaries) -> list:
    import aws_sdk_voice_id.types.speaker_enrollment_job_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_voice_id.types.speaker_enrollment_job_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SpeakerEnrollmentJobSummaries:
    import aws_sdk_voice_id.types.speaker_enrollment_job_summary

    out: SpeakerEnrollmentJobSummaries = []
    for item in data:
        out.append(
            aws_sdk_voice_id.types.speaker_enrollment_job_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
