"""Generated from Smithy shape ``com.amazonaws.transcribe#DeleteMedicalScribeJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.transcription_job_name


class DeleteMedicalScribeJobRequest(TypedDict, closed=True):
    medical_scribe_job_name: (
        "aws_sdk_transcribe.types.transcription_job_name.TranscriptionJobName"
    )
    """<p>The name of the Medical Scribe job you want to delete. Job names are case sensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMedicalScribeJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMedicalScribeJobRequest:
    out: DeleteMedicalScribeJobRequest = {}  # type: ignore[typeddict-item]
    return out
