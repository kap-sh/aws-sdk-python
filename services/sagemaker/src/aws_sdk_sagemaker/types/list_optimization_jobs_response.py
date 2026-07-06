"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListOptimizationJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.optimization_job_summaries


class ListOptimizationJobsResponse(TypedDict, closed=True):
    optimization_job_summaries: NotRequired[
        "aws_sdk_sagemaker.types.optimization_job_summaries.OptimizationJobSummaries"
    ]
    """<p>A list of optimization jobs and their properties that matches any of the filters you specified in the request.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>The token to use in a subsequent request to get the next set of results following a truncated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOptimizationJobsResponse) -> dict:
    out: dict = {}
    if "optimization_job_summaries" in value:
        import aws_sdk_sagemaker.types.optimization_job_summaries

        out["OptimizationJobSummaries"] = (
            aws_sdk_sagemaker.types.optimization_job_summaries.serialize_aws_json_1_1(
                value["optimization_job_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOptimizationJobsResponse:
    out: ListOptimizationJobsResponse = {}  # type: ignore[typeddict-item]
    if "OptimizationJobSummaries" in data:
        import aws_sdk_sagemaker.types.optimization_job_summaries

        out["optimization_job_summaries"] = (
            aws_sdk_sagemaker.types.optimization_job_summaries.deserialize_aws_json_1_1(
                data["OptimizationJobSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
