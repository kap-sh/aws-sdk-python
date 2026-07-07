"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.environment_parameters
    import aws_sdk_sagemaker.types.inference_specification_name
    import aws_sdk_sagemaker.types.recommendation_job_compilation_job_name


class ModelConfiguration(TypedDict, closed=True):
    inference_specification_name: NotRequired[
        "aws_sdk_sagemaker.types.inference_specification_name.InferenceSpecificationName"
    ]
    """<p>The inference specification name in the model package version.</p>"""
    environment_parameters: NotRequired[
        "aws_sdk_sagemaker.types.environment_parameters.EnvironmentParameters"
    ]
    """<p>Defines the environment parameters that includes key, value types, and values.</p>"""
    compilation_job_name: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_compilation_job_name.RecommendationJobCompilationJobName"
    ]
    """<p>The name of the compilation job used to create the recommended model artifacts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelConfiguration) -> dict:
    out: dict = {}
    if "inference_specification_name" in value:
        out["InferenceSpecificationName"] = value["inference_specification_name"]
    if "environment_parameters" in value:
        import aws_sdk_sagemaker.types.environment_parameters

        out["EnvironmentParameters"] = (
            aws_sdk_sagemaker.types.environment_parameters.serialize_aws_json_1_1(
                value["environment_parameters"]
            )
        )
    if "compilation_job_name" in value:
        out["CompilationJobName"] = value["compilation_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelConfiguration:
    out: ModelConfiguration = {}  # type: ignore[typeddict-item]
    if "InferenceSpecificationName" in data:
        out["inference_specification_name"] = data["InferenceSpecificationName"]
    if "EnvironmentParameters" in data:
        import aws_sdk_sagemaker.types.environment_parameters

        out["environment_parameters"] = (
            aws_sdk_sagemaker.types.environment_parameters.deserialize_aws_json_1_1(
                data["EnvironmentParameters"]
            )
        )
    if "CompilationJobName" in data:
        out["compilation_job_name"] = data["CompilationJobName"]
    return out
