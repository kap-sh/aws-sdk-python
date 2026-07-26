"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListInferenceRecommendationsJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_recommendations_jobs
    import capo_sagemaker.types.next_token


class ListInferenceRecommendationsJobsResponse(TypedDict, closed=True):
    inference_recommendations_jobs: NotRequired[
        "capo_sagemaker.types.inference_recommendations_jobs.InferenceRecommendationsJobs"
    ]
    """<p>The recommendations created from the Amazon SageMaker Inference Recommender job.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token for getting the next set of recommendations, if there are any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInferenceRecommendationsJobsResponse) -> dict:
    out: dict = {}
    if "inference_recommendations_jobs" in value:
        import capo_sagemaker.types.inference_recommendations_jobs

        out["InferenceRecommendationsJobs"] = (
            capo_sagemaker.types.inference_recommendations_jobs.serialize_aws_json_1_1(
                value["inference_recommendations_jobs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInferenceRecommendationsJobsResponse:
    out: ListInferenceRecommendationsJobsResponse = {}  # type: ignore[typeddict-item]
    if "InferenceRecommendationsJobs" in data:
        import capo_sagemaker.types.inference_recommendations_jobs

        out["inference_recommendations_jobs"] = (
            capo_sagemaker.types.inference_recommendations_jobs.deserialize_aws_json_1_1(
                data["InferenceRecommendationsJobs"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
