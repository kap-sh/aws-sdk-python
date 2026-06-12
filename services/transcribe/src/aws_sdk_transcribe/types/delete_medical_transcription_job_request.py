"""Generated from Smithy shape ``com.amazonaws.transcribe#DeleteMedicalTranscriptionJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.transcription_job_name


class DeleteMedicalTranscriptionJobRequest(TypedDict):
    medical_transcription_job_name: (
        "aws_sdk_transcribe.types.transcription_job_name.TranscriptionJobName"
    )
    """<p>The name of the medical transcription job you want to delete. Job names are case sensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMedicalTranscriptionJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMedicalTranscriptionJobRequest:
    out: DeleteMedicalTranscriptionJobRequest = {}  # type: ignore[typeddict-item]
    return out
