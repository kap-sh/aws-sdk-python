"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_benchmark_job_arn
    import aws_sdk_sagemaker.types.ai_recommendation_deployment_configuration
    import aws_sdk_sagemaker.types.ai_recommendation_model_details
    import aws_sdk_sagemaker.types.ai_recommendation_optimization_detail_list
    import aws_sdk_sagemaker.types.expected_performance_list
    import aws_sdk_sagemaker.types.string


class AIRecommendation(TypedDict):
    recommendation_description: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>A description of the recommendation.</p>"""
    optimization_details: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_optimization_detail_list.AIRecommendationOptimizationDetailList"
    ]
    """<p>The optimization techniques applied in this recommendation.</p>"""
    model_details: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_model_details.AIRecommendationModelDetails"
    ]
    """<p>Details about the model package associated with this recommendation.</p>"""
    deployment_configuration: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_deployment_configuration.AIRecommendationDeploymentConfiguration"
    ]
    """<p>The deployment configuration for this recommendation, including the container image, instance type, instance count, and environment variables.</p>"""
    ai_benchmark_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.ai_benchmark_job_arn.AIBenchmarkJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the benchmark job associated with this recommendation.</p>"""
    expected_performance: NotRequired[
        "aws_sdk_sagemaker.types.expected_performance_list.ExpectedPerformanceList"
    ]
    """<p>The expected performance metrics for this recommendation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendation) -> dict:
    out: dict = {}
    if "recommendation_description" in value:
        out["RecommendationDescription"] = value["recommendation_description"]
    if "optimization_details" in value:
        import aws_sdk_sagemaker.types.ai_recommendation_optimization_detail_list

        out["OptimizationDetails"] = (
            aws_sdk_sagemaker.types.ai_recommendation_optimization_detail_list.serialize_aws_json_1_1(
                value["optimization_details"]
            )
        )
    if "model_details" in value:
        import aws_sdk_sagemaker.types.ai_recommendation_model_details

        out["ModelDetails"] = (
            aws_sdk_sagemaker.types.ai_recommendation_model_details.serialize_aws_json_1_1(
                value["model_details"]
            )
        )
    if "deployment_configuration" in value:
        import aws_sdk_sagemaker.types.ai_recommendation_deployment_configuration

        out["DeploymentConfiguration"] = (
            aws_sdk_sagemaker.types.ai_recommendation_deployment_configuration.serialize_aws_json_1_1(
                value["deployment_configuration"]
            )
        )
    if "ai_benchmark_job_arn" in value:
        out["AIBenchmarkJobArn"] = value["ai_benchmark_job_arn"]
    if "expected_performance" in value:
        import aws_sdk_sagemaker.types.expected_performance_list

        out["ExpectedPerformance"] = (
            aws_sdk_sagemaker.types.expected_performance_list.serialize_aws_json_1_1(
                value["expected_performance"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIRecommendation:
    out: AIRecommendation = {}  # type: ignore[typeddict-item]
    if "RecommendationDescription" in data:
        out["recommendation_description"] = data["RecommendationDescription"]
    if "OptimizationDetails" in data:
        import aws_sdk_sagemaker.types.ai_recommendation_optimization_detail_list

        out["optimization_details"] = (
            aws_sdk_sagemaker.types.ai_recommendation_optimization_detail_list.deserialize_aws_json_1_1(
                data["OptimizationDetails"]
            )
        )
    if "ModelDetails" in data:
        import aws_sdk_sagemaker.types.ai_recommendation_model_details

        out["model_details"] = (
            aws_sdk_sagemaker.types.ai_recommendation_model_details.deserialize_aws_json_1_1(
                data["ModelDetails"]
            )
        )
    if "DeploymentConfiguration" in data:
        import aws_sdk_sagemaker.types.ai_recommendation_deployment_configuration

        out["deployment_configuration"] = (
            aws_sdk_sagemaker.types.ai_recommendation_deployment_configuration.deserialize_aws_json_1_1(
                data["DeploymentConfiguration"]
            )
        )
    if "AIBenchmarkJobArn" in data:
        out["ai_benchmark_job_arn"] = data["AIBenchmarkJobArn"]
    if "ExpectedPerformance" in data:
        import aws_sdk_sagemaker.types.expected_performance_list

        out["expected_performance"] = (
            aws_sdk_sagemaker.types.expected_performance_list.deserialize_aws_json_1_1(
                data["ExpectedPerformance"]
            )
        )
    return out
