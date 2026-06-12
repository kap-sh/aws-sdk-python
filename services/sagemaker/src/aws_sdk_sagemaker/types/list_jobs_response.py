"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.job_summaries
    import aws_sdk_sagemaker.types.next_token


class ListJobsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, this token retrieves the next set of results.</p>"""
    job_summaries: NotRequired["aws_sdk_sagemaker.types.job_summaries.JobSummaries"]
    """<p>An array of <code>JobSummary</code> objects that provide summary information about the jobs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "job_summaries" in value:
        import aws_sdk_sagemaker.types.job_summaries

        out["JobSummaries"] = (
            aws_sdk_sagemaker.types.job_summaries.serialize_aws_json_1_1(
                value["job_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListJobsResponse:
    out: ListJobsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "JobSummaries" in data:
        import aws_sdk_sagemaker.types.job_summaries

        out["job_summaries"] = (
            aws_sdk_sagemaker.types.job_summaries.deserialize_aws_json_1_1(
                data["JobSummaries"]
            )
        )
    return out
