"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateAIRecommendationJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_entity_name
    import aws_sdk_sagemaker.types.ai_model_source
    import aws_sdk_sagemaker.types.ai_recommendation_allow_optimization
    import aws_sdk_sagemaker.types.ai_recommendation_compute_spec
    import aws_sdk_sagemaker.types.ai_recommendation_inference_specification
    import aws_sdk_sagemaker.types.ai_recommendation_output_config
    import aws_sdk_sagemaker.types.ai_recommendation_performance_target
    import aws_sdk_sagemaker.types.ai_resource_identifier
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.tag_list


class CreateAIRecommendationJobRequest(TypedDict):
    ai_recommendation_job_name: NotRequired[
        "aws_sdk_sagemaker.types.ai_entity_name.AIEntityName"
    ]
    """<p>The name of the AI recommendation job. The name must be unique within your Amazon Web Services account in the current Amazon Web Services Region.</p>"""
    model_source: NotRequired["aws_sdk_sagemaker.types.ai_model_source.AIModelSource"]
    """<p>The source of the model to optimize. Specify the Amazon S3 location of the model artifacts.</p>"""
    output_config: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_output_config.AIRecommendationOutputConfig"
    ]
    """<p>The output configuration for the recommendation job, including the Amazon S3 location for results and an optional model package group where the optimized model is registered.</p>"""
    ai_workload_config_identifier: NotRequired[
        "aws_sdk_sagemaker.types.ai_resource_identifier.AIResourceIdentifier"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the AI workload configuration to use for this recommendation job.</p>"""
    performance_target: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_performance_target.AIRecommendationPerformanceTarget"
    ]
    """<p>The performance targets for the recommendation job. Specify constraints on metrics such as time to first token (<code>ttft-ms</code>), <code>throughput</code>, or <code>cost</code>.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker AI to perform tasks on your behalf.</p>"""
    inference_specification: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_inference_specification.AIRecommendationInferenceSpecification"
    ]
    """<p>The inference framework configuration. Specify the framework (such as LMI or vLLM) for the recommendation job.</p>"""
    optimize_model: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_allow_optimization.AIRecommendationAllowOptimization"
    ]
    """<p>Whether to allow model optimization techniques such as quantization, speculative decoding, and kernel tuning. The default is <code>true</code>.</p>"""
    compute_spec: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_compute_spec.AIRecommendationComputeSpec"
    ]
    """<p>The compute resource specification for the recommendation job. You can specify up to 3 instance types to consider, and optionally provide capacity reservation configuration.</p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    """<p>The metadata that you apply to Amazon Web Services resources to help you categorize and organize them.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAIRecommendationJobRequest) -> dict:
    out: dict = {}
    if "ai_recommendation_job_name" in value:
        out["AIRecommendationJobName"] = value["ai_recommendation_job_name"]
    if "model_source" in value:
        import aws_sdk_sagemaker.types.ai_model_source

        out["ModelSource"] = (
            aws_sdk_sagemaker.types.ai_model_source.serialize_aws_json_1_1(
                value["model_source"]
            )
        )
    if "output_config" in value:
        import aws_sdk_sagemaker.types.ai_recommendation_output_config

        out["OutputConfig"] = (
            aws_sdk_sagemaker.types.ai_recommendation_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    if "ai_workload_config_identifier" in value:
        out["AIWorkloadConfigIdentifier"] = value["ai_workload_config_identifier"]
    if "performance_target" in value:
        import aws_sdk_sagemaker.types.ai_recommendation_performance_target

        out["PerformanceTarget"] = (
            aws_sdk_sagemaker.types.ai_recommendation_performance_target.serialize_aws_json_1_1(
                value["performance_target"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "inference_specification" in value:
        import aws_sdk_sagemaker.types.ai_recommendation_inference_specification

        out["InferenceSpecification"] = (
            aws_sdk_sagemaker.types.ai_recommendation_inference_specification.serialize_aws_json_1_1(
                value["inference_specification"]
            )
        )
    if "optimize_model" in value:
        out["OptimizeModel"] = value["optimize_model"]
    if "compute_spec" in value:
        import aws_sdk_sagemaker.types.ai_recommendation_compute_spec

        out["ComputeSpec"] = (
            aws_sdk_sagemaker.types.ai_recommendation_compute_spec.serialize_aws_json_1_1(
                value["compute_spec"]
            )
        )
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAIRecommendationJobRequest:
    out: CreateAIRecommendationJobRequest = {}  # type: ignore[typeddict-item]
    if "AIRecommendationJobName" in data:
        out["ai_recommendation_job_name"] = data["AIRecommendationJobName"]
    if "ModelSource" in data:
        import aws_sdk_sagemaker.types.ai_model_source

        out["model_source"] = (
            aws_sdk_sagemaker.types.ai_model_source.deserialize_aws_json_1_1(
                data["ModelSource"]
            )
        )
    if "OutputConfig" in data:
        import aws_sdk_sagemaker.types.ai_recommendation_output_config

        out["output_config"] = (
            aws_sdk_sagemaker.types.ai_recommendation_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if "AIWorkloadConfigIdentifier" in data:
        out["ai_workload_config_identifier"] = data["AIWorkloadConfigIdentifier"]
    if "PerformanceTarget" in data:
        import aws_sdk_sagemaker.types.ai_recommendation_performance_target

        out["performance_target"] = (
            aws_sdk_sagemaker.types.ai_recommendation_performance_target.deserialize_aws_json_1_1(
                data["PerformanceTarget"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "InferenceSpecification" in data:
        import aws_sdk_sagemaker.types.ai_recommendation_inference_specification

        out["inference_specification"] = (
            aws_sdk_sagemaker.types.ai_recommendation_inference_specification.deserialize_aws_json_1_1(
                data["InferenceSpecification"]
            )
        )
    if "OptimizeModel" in data:
        out["optimize_model"] = data["OptimizeModel"]
    if "ComputeSpec" in data:
        import aws_sdk_sagemaker.types.ai_recommendation_compute_spec

        out["compute_spec"] = (
            aws_sdk_sagemaker.types.ai_recommendation_compute_spec.deserialize_aws_json_1_1(
                data["ComputeSpec"]
            )
        )
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
