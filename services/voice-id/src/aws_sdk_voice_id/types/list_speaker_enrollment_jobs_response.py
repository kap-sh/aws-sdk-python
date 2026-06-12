"""Generated from Smithy shape ``com.amazonaws.voiceid#ListSpeakerEnrollmentJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.speaker_enrollment_job_summaries
    import aws_sdk_voice_id.types.string


class ListSpeakerEnrollmentJobsResponse(TypedDict):
    job_summaries: NotRequired[
        "aws_sdk_voice_id.types.speaker_enrollment_job_summaries.SpeakerEnrollmentJobSummaries"
    ]
    """<p>A list containing details about each specified speaker enrollment job.</p>"""
    next_token: NotRequired["aws_sdk_voice_id.types.string.String"]
    """<p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSpeakerEnrollmentJobsResponse) -> dict:
    out: dict = {}
    if "job_summaries" in value:
        import aws_sdk_voice_id.types.speaker_enrollment_job_summaries

        out["JobSummaries"] = (
            aws_sdk_voice_id.types.speaker_enrollment_job_summaries.serialize_aws_json_1_0(
                value["job_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSpeakerEnrollmentJobsResponse:
    out: ListSpeakerEnrollmentJobsResponse = {}  # type: ignore[typeddict-item]
    if "JobSummaries" in data:
        import aws_sdk_voice_id.types.speaker_enrollment_job_summaries

        out["job_summaries"] = (
            aws_sdk_voice_id.types.speaker_enrollment_job_summaries.deserialize_aws_json_1_0(
                data["JobSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
