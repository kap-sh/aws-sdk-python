"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListInferenceRecommendationsJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.inference_recommendations_jobs
    import aws_sdk_sagemaker.types.next_token


class ListInferenceRecommendationsJobsResponse(TypedDict):
    inference_recommendations_jobs: NotRequired[
        "aws_sdk_sagemaker.types.inference_recommendations_jobs.InferenceRecommendationsJobs"
    ]
    """<p>The recommendations created from the Amazon SageMaker Inference Recommender job.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>A token for getting the next set of recommendations, if there are any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInferenceRecommendationsJobsResponse) -> dict:
    out: dict = {}
    if "inference_recommendations_jobs" in value:
        import aws_sdk_sagemaker.types.inference_recommendations_jobs

        out["InferenceRecommendationsJobs"] = (
            aws_sdk_sagemaker.types.inference_recommendations_jobs.serialize_aws_json_1_1(
                value["inference_recommendations_jobs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInferenceRecommendationsJobsResponse:
    out: ListInferenceRecommendationsJobsResponse = {}  # type: ignore[typeddict-item]
    if "InferenceRecommendationsJobs" in data:
        import aws_sdk_sagemaker.types.inference_recommendations_jobs

        out["inference_recommendations_jobs"] = (
            aws_sdk_sagemaker.types.inference_recommendations_jobs.deserialize_aws_json_1_1(
                data["InferenceRecommendationsJobs"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
