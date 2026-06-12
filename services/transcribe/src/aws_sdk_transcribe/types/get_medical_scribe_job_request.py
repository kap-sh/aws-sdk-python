"""Generated from Smithy shape ``com.amazonaws.transcribe#GetMedicalScribeJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.transcription_job_name


class GetMedicalScribeJobRequest(TypedDict):
    medical_scribe_job_name: (
        "aws_sdk_transcribe.types.transcription_job_name.TranscriptionJobName"
    )
    """<p>The name of the Medical Scribe job you want information about. Job names are case sensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMedicalScribeJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMedicalScribeJobRequest:
    out: GetMedicalScribeJobRequest = {}  # type: ignore[typeddict-item]
    return out
