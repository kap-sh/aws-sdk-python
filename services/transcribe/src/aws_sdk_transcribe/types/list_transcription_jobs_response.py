"""Generated from Smithy shape ``com.amazonaws.transcribe#ListTranscriptionJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.next_token
    import aws_sdk_transcribe.types.transcription_job_status
    import aws_sdk_transcribe.types.transcription_job_summaries


class ListTranscriptionJobsResponse(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_transcribe.types.transcription_job_status.TranscriptionJobStatus"
    ]
    """<p>Lists all transcription jobs that have the status specified in your request. Jobs are ordered by creation date, with the newest job first.</p>"""
    next_token: NotRequired["aws_sdk_transcribe.types.next_token.NextToken"]
    """<p>If <code>NextToken</code> is present in your response, it indicates that not all results are displayed. To view the next set of results, copy the string associated with the <code>NextToken</code> parameter in your results output, then run your request again including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>"""
    transcription_job_summaries: NotRequired[
        "aws_sdk_transcribe.types.transcription_job_summaries.TranscriptionJobSummaries"
    ]
    """<p>Provides a summary of information about each result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTranscriptionJobsResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_transcribe.types.transcription_job_status

        out["Status"] = (
            aws_sdk_transcribe.types.transcription_job_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "transcription_job_summaries" in value:
        import aws_sdk_transcribe.types.transcription_job_summaries

        out["TranscriptionJobSummaries"] = (
            aws_sdk_transcribe.types.transcription_job_summaries.serialize_aws_json_1_1(
                value["transcription_job_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTranscriptionJobsResponse:
    out: ListTranscriptionJobsResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_transcribe.types.transcription_job_status

        out["status"] = (
            aws_sdk_transcribe.types.transcription_job_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "TranscriptionJobSummaries" in data:
        import aws_sdk_transcribe.types.transcription_job_summaries

        out["transcription_job_summaries"] = (
            aws_sdk_transcribe.types.transcription_job_summaries.deserialize_aws_json_1_1(
                data["TranscriptionJobSummaries"]
            )
        )
    return out
