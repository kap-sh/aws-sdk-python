"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceRecommendationsJobStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.recommendation_job_inference_benchmark
    import aws_sdk_sagemaker.types.recommendation_job_name
    import aws_sdk_sagemaker.types.recommendation_job_status
    import aws_sdk_sagemaker.types.recommendation_step_type


class InferenceRecommendationsJobStep(TypedDict, closed=True):
    step_type: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_step_type.RecommendationStepType"
    ]
    """<p>The type of the subtask.</p> <p> <code>BENCHMARK</code>: Evaluate the performance of your model on different instance types.</p>"""
    job_name: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_name.RecommendationJobName"
    ]
    """<p>The name of the Inference Recommender job.</p>"""
    status: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_status.RecommendationJobStatus"
    ]
    """<p>The current status of the benchmark.</p>"""
    inference_benchmark: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_inference_benchmark.RecommendationJobInferenceBenchmark"
    ]
    """<p>The details for a specific benchmark.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceRecommendationsJobStep) -> dict:
    out: dict = {}
    if "step_type" in value:
        import aws_sdk_sagemaker.types.recommendation_step_type

        out["StepType"] = (
            aws_sdk_sagemaker.types.recommendation_step_type.serialize_aws_json_1_1(
                value["step_type"]
            )
        )
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "status" in value:
        import aws_sdk_sagemaker.types.recommendation_job_status

        out["Status"] = (
            aws_sdk_sagemaker.types.recommendation_job_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "inference_benchmark" in value:
        import aws_sdk_sagemaker.types.recommendation_job_inference_benchmark

        out["InferenceBenchmark"] = (
            aws_sdk_sagemaker.types.recommendation_job_inference_benchmark.serialize_aws_json_1_1(
                value["inference_benchmark"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceRecommendationsJobStep:
    out: InferenceRecommendationsJobStep = {}  # type: ignore[typeddict-item]
    if "StepType" in data:
        import aws_sdk_sagemaker.types.recommendation_step_type

        out["step_type"] = (
            aws_sdk_sagemaker.types.recommendation_step_type.deserialize_aws_json_1_1(
                data["StepType"]
            )
        )
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "Status" in data:
        import aws_sdk_sagemaker.types.recommendation_job_status

        out["status"] = (
            aws_sdk_sagemaker.types.recommendation_job_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "InferenceBenchmark" in data:
        import aws_sdk_sagemaker.types.recommendation_job_inference_benchmark

        out["inference_benchmark"] = (
            aws_sdk_sagemaker.types.recommendation_job_inference_benchmark.deserialize_aws_json_1_1(
                data["InferenceBenchmark"]
            )
        )
    return out
