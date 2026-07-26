"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribeJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.medical_scribe_job_summary

MedicalScribeJobSummaries: TypeAlias = list[
    "capo_transcribe.types.medical_scribe_job_summary.MedicalScribeJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalScribeJobSummaries) -> list:
    import capo_transcribe.types.medical_scribe_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_transcribe.types.medical_scribe_job_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MedicalScribeJobSummaries:
    import capo_transcribe.types.medical_scribe_job_summary

    out: MedicalScribeJobSummaries = []
    for item in data:
        out.append(
            capo_transcribe.types.medical_scribe_job_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
