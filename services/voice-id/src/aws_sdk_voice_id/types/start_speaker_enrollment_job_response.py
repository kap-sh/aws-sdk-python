"""Generated from Smithy shape ``com.amazonaws.voiceid#StartSpeakerEnrollmentJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.speaker_enrollment_job


class StartSpeakerEnrollmentJobResponse(TypedDict):
    job: NotRequired[
        "aws_sdk_voice_id.types.speaker_enrollment_job.SpeakerEnrollmentJob"
    ]
    """<p>Details about the started speaker enrollment job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartSpeakerEnrollmentJobResponse) -> dict:
    out: dict = {}
    if "job" in value:
        import aws_sdk_voice_id.types.speaker_enrollment_job

        out["Job"] = (
            aws_sdk_voice_id.types.speaker_enrollment_job.serialize_aws_json_1_0(
                value["job"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartSpeakerEnrollmentJobResponse:
    out: StartSpeakerEnrollmentJobResponse = {}  # type: ignore[typeddict-item]
    if "Job" in data:
        import aws_sdk_voice_id.types.speaker_enrollment_job

        out["job"] = (
            aws_sdk_voice_id.types.speaker_enrollment_job.deserialize_aws_json_1_0(
                data["Job"]
            )
        )
    return out
