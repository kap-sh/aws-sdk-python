"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAutoMLJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_job_summaries
    import aws_sdk_sagemaker.types.next_token


class ListAutoMLJobsResponse(TypedDict, closed=True):
    auto_ml_job_summaries: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_job_summaries.AutoMLJobSummaries"
    ]
    """<p>Returns a summary list of jobs.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAutoMLJobsResponse) -> dict:
    out: dict = {}
    if "auto_ml_job_summaries" in value:
        import aws_sdk_sagemaker.types.auto_ml_job_summaries

        out["AutoMLJobSummaries"] = (
            aws_sdk_sagemaker.types.auto_ml_job_summaries.serialize_aws_json_1_1(
                value["auto_ml_job_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAutoMLJobsResponse:
    out: ListAutoMLJobsResponse = {}  # type: ignore[typeddict-item]
    if "AutoMLJobSummaries" in data:
        import aws_sdk_sagemaker.types.auto_ml_job_summaries

        out["auto_ml_job_summaries"] = (
            aws_sdk_sagemaker.types.auto_ml_job_summaries.deserialize_aws_json_1_1(
                data["AutoMLJobSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
