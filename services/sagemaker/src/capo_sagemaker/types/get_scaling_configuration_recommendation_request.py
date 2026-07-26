"""Generated from Smithy shape ``com.amazonaws.sagemaker#GetScalingConfigurationRecommendationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_name
    import capo_sagemaker.types.recommendation_job_name
    import capo_sagemaker.types.scaling_policy_objective
    import capo_sagemaker.types.string
    import capo_sagemaker.types.utilization_percentage_per_core


class GetScalingConfigurationRecommendationRequest(TypedDict, closed=True):
    inference_recommendations_job_name: NotRequired[
        "capo_sagemaker.types.recommendation_job_name.RecommendationJobName"
    ]
    """<p>The name of a previously completed Inference Recommender job.</p>"""
    recommendation_id: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The recommendation ID of a previously completed inference recommendation. This ID should come from one of the recommendations returned by the job specified in the <code>InferenceRecommendationsJobName</code> field.</p> <p>Specify either this field or the <code>EndpointName</code> field.</p>"""
    endpoint_name: NotRequired["capo_sagemaker.types.endpoint_name.EndpointName"]
    """<p>The name of an endpoint benchmarked during a previously completed inference recommendation job. This name should come from one of the recommendations returned by the job specified in the <code>InferenceRecommendationsJobName</code> field.</p> <p>Specify either this field or the <code>RecommendationId</code> field.</p>"""
    target_cpu_utilization_per_core: NotRequired[
        "capo_sagemaker.types.utilization_percentage_per_core.UtilizationPercentagePerCore"
    ]
    """<p>The percentage of how much utilization you want an instance to use before autoscaling. The default value is 50%.</p>"""
    scaling_policy_objective: NotRequired[
        "capo_sagemaker.types.scaling_policy_objective.ScalingPolicyObjective"
    ]
    """<p>An object where you specify the anticipated traffic pattern for an endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetScalingConfigurationRecommendationRequest) -> dict:
    out: dict = {}
    if "inference_recommendations_job_name" in value:
        out["InferenceRecommendationsJobName"] = value[
            "inference_recommendations_job_name"
        ]
    if "recommendation_id" in value:
        out["RecommendationId"] = value["recommendation_id"]
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "target_cpu_utilization_per_core" in value:
        out["TargetCpuUtilizationPerCore"] = value["target_cpu_utilization_per_core"]
    if "scaling_policy_objective" in value:
        import capo_sagemaker.types.scaling_policy_objective

        out["ScalingPolicyObjective"] = (
            capo_sagemaker.types.scaling_policy_objective.serialize_aws_json_1_1(
                value["scaling_policy_objective"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetScalingConfigurationRecommendationRequest:
    out: GetScalingConfigurationRecommendationRequest = {}  # type: ignore[typeddict-item]
    if "InferenceRecommendationsJobName" in data:
        out["inference_recommendations_job_name"] = data[
            "InferenceRecommendationsJobName"
        ]
    if "RecommendationId" in data:
        out["recommendation_id"] = data["RecommendationId"]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    if "TargetCpuUtilizationPerCore" in data:
        out["target_cpu_utilization_per_core"] = data["TargetCpuUtilizationPerCore"]
    if "ScalingPolicyObjective" in data:
        import capo_sagemaker.types.scaling_policy_objective

        out["scaling_policy_objective"] = (
            capo_sagemaker.types.scaling_policy_objective.deserialize_aws_json_1_1(
                data["ScalingPolicyObjective"]
            )
        )
    return out
