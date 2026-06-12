"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAIBenchmarkJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_benchmark_job_summary_list
    import aws_sdk_sagemaker.types.next_token


class ListAIBenchmarkJobsResponse(TypedDict):
    ai_benchmark_jobs: NotRequired[
        "aws_sdk_sagemaker.types.ai_benchmark_job_summary_list.AIBenchmarkJobSummaryList"
    ]
    """<p>An array of <code>AIBenchmarkJobSummary</code> objects, one for each benchmark job that matches the specified filters.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon SageMaker AI returns this token. To retrieve the next set of jobs, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAIBenchmarkJobsResponse) -> dict:
    out: dict = {}
    if "ai_benchmark_jobs" in value:
        import aws_sdk_sagemaker.types.ai_benchmark_job_summary_list

        out["AIBenchmarkJobs"] = (
            aws_sdk_sagemaker.types.ai_benchmark_job_summary_list.serialize_aws_json_1_1(
                value["ai_benchmark_jobs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAIBenchmarkJobsResponse:
    out: ListAIBenchmarkJobsResponse = {}  # type: ignore[typeddict-item]
    if "AIBenchmarkJobs" in data:
        import aws_sdk_sagemaker.types.ai_benchmark_job_summary_list

        out["ai_benchmark_jobs"] = (
            aws_sdk_sagemaker.types.ai_benchmark_job_summary_list.deserialize_aws_json_1_1(
                data["AIBenchmarkJobs"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
