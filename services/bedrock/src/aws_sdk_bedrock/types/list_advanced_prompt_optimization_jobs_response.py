"""Generated from Smithy shape ``com.amazonaws.bedrock#ListAdvancedPromptOptimizationJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.advanced_prompt_optimization_job_summaries
    import aws_sdk_bedrock.types.pagination_token


class ListAdvancedPromptOptimizationJobsResponse(TypedDict):
    job_summaries: NotRequired[
        "aws_sdk_bedrock.types.advanced_prompt_optimization_job_summaries.AdvancedPromptOptimizationJobSummaries"
    ]
    """<p>A list of advanced prompt optimization job summaries.</p>"""
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token in a subsequent request to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAdvancedPromptOptimizationJobsResponse) -> dict:
    out: dict = {}
    if "job_summaries" in value:
        import aws_sdk_bedrock.types.advanced_prompt_optimization_job_summaries

        out["jobSummaries"] = (
            aws_sdk_bedrock.types.advanced_prompt_optimization_job_summaries.serialize_json(
                value["job_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAdvancedPromptOptimizationJobsResponse:
    out: ListAdvancedPromptOptimizationJobsResponse = {}  # type: ignore[typeddict-item]
    if "jobSummaries" in data:
        import aws_sdk_bedrock.types.advanced_prompt_optimization_job_summaries

        out["job_summaries"] = (
            aws_sdk_bedrock.types.advanced_prompt_optimization_job_summaries.deserialize_json(
                data["jobSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
