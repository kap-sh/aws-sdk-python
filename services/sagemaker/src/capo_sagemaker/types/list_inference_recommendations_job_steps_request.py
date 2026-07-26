"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListInferenceRecommendationsJobStepsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.recommendation_job_name
    import capo_sagemaker.types.recommendation_job_status
    import capo_sagemaker.types.recommendation_step_type


class ListInferenceRecommendationsJobStepsRequest(TypedDict, closed=True):
    job_name: NotRequired[
        "capo_sagemaker.types.recommendation_job_name.RecommendationJobName"
    ]
    """<p>The name for the Inference Recommender job.</p>"""
    status: NotRequired[
        "capo_sagemaker.types.recommendation_job_status.RecommendationJobStatus"
    ]
    """<p>A filter to return benchmarks of a specified status. If this field is left empty, then all benchmarks are returned.</p>"""
    step_type: NotRequired[
        "capo_sagemaker.types.recommendation_step_type.RecommendationStepType"
    ]
    """<p>A filter to return details about the specified type of subtask.</p> <p> <code>BENCHMARK</code>: Evaluate the performance of your model on different instance types.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token that you can specify to return more results from the list. Specify this field if you have a token that was returned from a previous request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInferenceRecommendationsJobStepsRequest) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "status" in value:
        import capo_sagemaker.types.recommendation_job_status

        out["Status"] = (
            capo_sagemaker.types.recommendation_job_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "step_type" in value:
        import capo_sagemaker.types.recommendation_step_type

        out["StepType"] = (
            capo_sagemaker.types.recommendation_step_type.serialize_aws_json_1_1(
                value["step_type"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInferenceRecommendationsJobStepsRequest:
    out: ListInferenceRecommendationsJobStepsRequest = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "Status" in data:
        import capo_sagemaker.types.recommendation_job_status

        out["status"] = (
            capo_sagemaker.types.recommendation_job_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StepType" in data:
        import capo_sagemaker.types.recommendation_step_type

        out["step_type"] = (
            capo_sagemaker.types.recommendation_step_type.deserialize_aws_json_1_1(
                data["StepType"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
