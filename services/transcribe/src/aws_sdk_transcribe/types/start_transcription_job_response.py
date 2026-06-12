"""Generated from Smithy shape ``com.amazonaws.transcribe#StartTranscriptionJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.transcription_job


class StartTranscriptionJobResponse(TypedDict):
    transcription_job: NotRequired[
        "aws_sdk_transcribe.types.transcription_job.TranscriptionJob"
    ]
    """<p>Provides detailed information about the current transcription job, including job status and, if applicable, failure reason.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartTranscriptionJobResponse) -> dict:
    out: dict = {}
    if "transcription_job" in value:
        import aws_sdk_transcribe.types.transcription_job

        out["TranscriptionJob"] = (
            aws_sdk_transcribe.types.transcription_job.serialize_aws_json_1_1(
                value["transcription_job"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartTranscriptionJobResponse:
    out: StartTranscriptionJobResponse = {}  # type: ignore[typeddict-item]
    if "TranscriptionJob" in data:
        import aws_sdk_transcribe.types.transcription_job

        out["transcription_job"] = (
            aws_sdk_transcribe.types.transcription_job.deserialize_aws_json_1_1(
                data["TranscriptionJob"]
            )
        )
    return out
