"""Generated from Smithy shape ``com.amazonaws.transcribe#GetMedicalScribeJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.medical_scribe_job


class GetMedicalScribeJobResponse(TypedDict):
    medical_scribe_job: NotRequired[
        "aws_sdk_transcribe.types.medical_scribe_job.MedicalScribeJob"
    ]
    """<p>Provides detailed information about the specified Medical Scribe job, including job status and, if applicable, failure reason</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMedicalScribeJobResponse) -> dict:
    out: dict = {}
    if "medical_scribe_job" in value:
        import aws_sdk_transcribe.types.medical_scribe_job

        out["MedicalScribeJob"] = (
            aws_sdk_transcribe.types.medical_scribe_job.serialize_aws_json_1_1(
                value["medical_scribe_job"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMedicalScribeJobResponse:
    out: GetMedicalScribeJobResponse = {}  # type: ignore[typeddict-item]
    if "MedicalScribeJob" in data:
        import aws_sdk_transcribe.types.medical_scribe_job

        out["medical_scribe_job"] = (
            aws_sdk_transcribe.types.medical_scribe_job.deserialize_aws_json_1_1(
                data["MedicalScribeJob"]
            )
        )
    return out
