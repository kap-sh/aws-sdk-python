"""Generated from Smithy shape ``com.amazonaws.transcribe#ListMedicalScribeJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.max_results
    import capo_transcribe.types.medical_scribe_job_status
    import capo_transcribe.types.next_token
    import capo_transcribe.types.transcription_job_name


class ListMedicalScribeJobsRequest(TypedDict, closed=True):
    status: NotRequired[
        "capo_transcribe.types.medical_scribe_job_status.MedicalScribeJobStatus"
    ]
    """<p>Returns only Medical Scribe jobs with the specified status. Jobs are ordered by creation date, with the newest job first. If you do not include <code>Status</code>, all Medical Scribe jobs are returned.</p>"""
    job_name_contains: NotRequired[
        "capo_transcribe.types.transcription_job_name.TranscriptionJobName"
    ]
    """<p>Returns only the Medical Scribe jobs that contain the specified string. The search is not case sensitive.</p>"""
    next_token: NotRequired["capo_transcribe.types.next_token.NextToken"]
    """<p>If your <code>ListMedicalScribeJobs</code> request returns more results than can be displayed, <code>NextToken</code> is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>"""
    max_results: NotRequired["capo_transcribe.types.max_results.MaxResults"]
    """<p>The maximum number of Medical Scribe jobs to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMedicalScribeJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMedicalScribeJobsRequest:
    out: ListMedicalScribeJobsRequest = {}  # type: ignore[typeddict-item]
    return out
