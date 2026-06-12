"""Generated from Smithy shape ``com.amazonaws.transcribe#ListMedicalTranscriptionJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.max_results
    import aws_sdk_transcribe.types.next_token
    import aws_sdk_transcribe.types.transcription_job_name
    import aws_sdk_transcribe.types.transcription_job_status


class ListMedicalTranscriptionJobsRequest(TypedDict):
    status: NotRequired[
        "aws_sdk_transcribe.types.transcription_job_status.TranscriptionJobStatus"
    ]
    """<p>Returns only medical transcription jobs with the specified status. Jobs are ordered by creation date, with the newest job first. If you do not include <code>Status</code>, all medical transcription jobs are returned.</p>"""
    job_name_contains: NotRequired[
        "aws_sdk_transcribe.types.transcription_job_name.TranscriptionJobName"
    ]
    """<p>Returns only the medical transcription jobs that contain the specified string. The search is not case sensitive.</p>"""
    next_token: NotRequired["aws_sdk_transcribe.types.next_token.NextToken"]
    """<p>If your <code>ListMedicalTranscriptionJobs</code> request returns more results than can be displayed, <code>NextToken</code> is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>"""
    max_results: NotRequired["aws_sdk_transcribe.types.max_results.MaxResults"]
    """<p>The maximum number of medical transcription jobs to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMedicalTranscriptionJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMedicalTranscriptionJobsRequest:
    out: ListMedicalTranscriptionJobsRequest = {}  # type: ignore[typeddict-item]
    return out
