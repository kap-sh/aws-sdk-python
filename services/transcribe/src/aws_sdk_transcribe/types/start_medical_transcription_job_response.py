"""Generated from Smithy shape ``com.amazonaws.transcribe#StartMedicalTranscriptionJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.medical_transcription_job


class StartMedicalTranscriptionJobResponse(TypedDict):
    medical_transcription_job: NotRequired[
        "aws_sdk_transcribe.types.medical_transcription_job.MedicalTranscriptionJob"
    ]
    """<p>Provides detailed information about the current medical transcription job, including job status and, if applicable, failure reason.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMedicalTranscriptionJobResponse) -> dict:
    out: dict = {}
    if "medical_transcription_job" in value:
        import aws_sdk_transcribe.types.medical_transcription_job

        out["MedicalTranscriptionJob"] = (
            aws_sdk_transcribe.types.medical_transcription_job.serialize_aws_json_1_1(
                value["medical_transcription_job"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMedicalTranscriptionJobResponse:
    out: StartMedicalTranscriptionJobResponse = {}  # type: ignore[typeddict-item]
    if "MedicalTranscriptionJob" in data:
        import aws_sdk_transcribe.types.medical_transcription_job

        out["medical_transcription_job"] = (
            aws_sdk_transcribe.types.medical_transcription_job.deserialize_aws_json_1_1(
                data["MedicalTranscriptionJob"]
            )
        )
    return out
