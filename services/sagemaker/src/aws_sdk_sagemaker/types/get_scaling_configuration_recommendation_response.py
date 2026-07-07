"""Generated from Smithy shape ``com.amazonaws.sagemaker#GetScalingConfigurationRecommendationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.dynamic_scaling_configuration
    import aws_sdk_sagemaker.types.endpoint_name
    import aws_sdk_sagemaker.types.recommendation_job_name
    import aws_sdk_sagemaker.types.scaling_policy_metric
    import aws_sdk_sagemaker.types.scaling_policy_objective
    import aws_sdk_sagemaker.types.string
    import aws_sdk_sagemaker.types.utilization_percentage_per_core


class GetScalingConfigurationRecommendationResponse(TypedDict, closed=True):
    inference_recommendations_job_name: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_name.RecommendationJobName"
    ]
    """<p>The name of a previously completed Inference Recommender job.</p>"""
    recommendation_id: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The recommendation ID of a previously completed inference recommendation.</p>"""
    endpoint_name: NotRequired["aws_sdk_sagemaker.types.endpoint_name.EndpointName"]
    """<p>The name of an endpoint benchmarked during a previously completed Inference Recommender job.</p>"""
    target_cpu_utilization_per_core: NotRequired[
        "aws_sdk_sagemaker.types.utilization_percentage_per_core.UtilizationPercentagePerCore"
    ]
    """<p>The percentage of how much utilization you want an instance to use before autoscaling, which you specified in the request. The default value is 50%.</p>"""
    scaling_policy_objective: NotRequired[
        "aws_sdk_sagemaker.types.scaling_policy_objective.ScalingPolicyObjective"
    ]
    """<p>An object representing the anticipated traffic pattern for an endpoint that you specified in the request.</p>"""
    metric: NotRequired[
        "aws_sdk_sagemaker.types.scaling_policy_metric.ScalingPolicyMetric"
    ]
    """<p>An object with a list of metrics that were benchmarked during the previously completed Inference Recommender job.</p>"""
    dynamic_scaling_configuration: NotRequired[
        "aws_sdk_sagemaker.types.dynamic_scaling_configuration.DynamicScalingConfiguration"
    ]
    """<p>An object with the recommended values for you to specify when creating an autoscaling policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetScalingConfigurationRecommendationResponse,
) -> dict:
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
        import aws_sdk_sagemaker.types.scaling_policy_objective

        out["ScalingPolicyObjective"] = (
            aws_sdk_sagemaker.types.scaling_policy_objective.serialize_aws_json_1_1(
                value["scaling_policy_objective"]
            )
        )
    if "metric" in value:
        import aws_sdk_sagemaker.types.scaling_policy_metric

        out["Metric"] = (
            aws_sdk_sagemaker.types.scaling_policy_metric.serialize_aws_json_1_1(
                value["metric"]
            )
        )
    if "dynamic_scaling_configuration" in value:
        import aws_sdk_sagemaker.types.dynamic_scaling_configuration

        out["DynamicScalingConfiguration"] = (
            aws_sdk_sagemaker.types.dynamic_scaling_configuration.serialize_aws_json_1_1(
                value["dynamic_scaling_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetScalingConfigurationRecommendationResponse:
    out: GetScalingConfigurationRecommendationResponse = {}  # type: ignore[typeddict-item]
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
        import aws_sdk_sagemaker.types.scaling_policy_objective

        out["scaling_policy_objective"] = (
            aws_sdk_sagemaker.types.scaling_policy_objective.deserialize_aws_json_1_1(
                data["ScalingPolicyObjective"]
            )
        )
    if "Metric" in data:
        import aws_sdk_sagemaker.types.scaling_policy_metric

        out["metric"] = (
            aws_sdk_sagemaker.types.scaling_policy_metric.deserialize_aws_json_1_1(
                data["Metric"]
            )
        )
    if "DynamicScalingConfiguration" in data:
        import aws_sdk_sagemaker.types.dynamic_scaling_configuration

        out["dynamic_scaling_configuration"] = (
            aws_sdk_sagemaker.types.dynamic_scaling_configuration.deserialize_aws_json_1_1(
                data["DynamicScalingConfiguration"]
            )
        )
    return out
