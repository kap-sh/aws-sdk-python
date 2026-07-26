"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListInferenceRecommendationsJobStepsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_recommendations_job_steps
    import capo_sagemaker.types.next_token


class ListInferenceRecommendationsJobStepsResponse(TypedDict, closed=True):
    steps: NotRequired[
        "capo_sagemaker.types.inference_recommendations_job_steps.InferenceRecommendationsJobSteps"
    ]
    """<p>A list of all subtask details in Inference Recommender.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token that you can specify in your next request to return more results from the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInferenceRecommendationsJobStepsResponse) -> dict:
    out: dict = {}
    if "steps" in value:
        import capo_sagemaker.types.inference_recommendations_job_steps

        out["Steps"] = (
            capo_sagemaker.types.inference_recommendations_job_steps.serialize_aws_json_1_1(
                value["steps"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListInferenceRecommendationsJobStepsResponse:
    out: ListInferenceRecommendationsJobStepsResponse = {}  # type: ignore[typeddict-item]
    if "Steps" in data:
        import capo_sagemaker.types.inference_recommendations_job_steps

        out["steps"] = (
            capo_sagemaker.types.inference_recommendations_job_steps.deserialize_aws_json_1_1(
                data["Steps"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
