"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalTranscriptionJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.medical_transcription_job_summary

MedicalTranscriptionJobSummaries: TypeAlias = list[
    "capo_transcribe.types.medical_transcription_job_summary.MedicalTranscriptionJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalTranscriptionJobSummaries) -> list:
    import capo_transcribe.types.medical_transcription_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_transcribe.types.medical_transcription_job_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MedicalTranscriptionJobSummaries:
    import capo_transcribe.types.medical_transcription_job_summary

    out: MedicalTranscriptionJobSummaries = []
    for item in data:
        out.append(
            capo_transcribe.types.medical_transcription_job_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
