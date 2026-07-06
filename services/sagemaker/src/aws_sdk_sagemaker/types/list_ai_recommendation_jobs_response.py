"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAIRecommendationJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_recommendation_job_summary_list
    import aws_sdk_sagemaker.types.next_token


class ListAIRecommendationJobsResponse(TypedDict, closed=True):
    ai_recommendation_jobs: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_job_summary_list.AIRecommendationJobSummaryList"
    ]
    """<p>An array of <code>AIRecommendationJobSummary</code> objects, one for each recommendation job that matches the specified filters.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon SageMaker AI returns this token. To retrieve the next set of jobs, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAIRecommendationJobsResponse) -> dict:
    out: dict = {}
    if "ai_recommendation_jobs" in value:
        import aws_sdk_sagemaker.types.ai_recommendation_job_summary_list

        out["AIRecommendationJobs"] = (
            aws_sdk_sagemaker.types.ai_recommendation_job_summary_list.serialize_aws_json_1_1(
                value["ai_recommendation_jobs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAIRecommendationJobsResponse:
    out: ListAIRecommendationJobsResponse = {}  # type: ignore[typeddict-item]
    if "AIRecommendationJobs" in data:
        import aws_sdk_sagemaker.types.ai_recommendation_job_summary_list

        out["ai_recommendation_jobs"] = (
            aws_sdk_sagemaker.types.ai_recommendation_job_summary_list.deserialize_aws_json_1_1(
                data["AIRecommendationJobs"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
