"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelShardingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.optimization_container_image
    import capo_sagemaker.types.optimization_job_environment_variables


class ModelShardingConfig(TypedDict, closed=True):
    image: NotRequired[
        "capo_sagemaker.types.optimization_container_image.OptimizationContainerImage"
    ]
    """<p>The URI of an LMI DLC in Amazon ECR. SageMaker uses this image to run the optimization.</p>"""
    override_environment: NotRequired[
        "capo_sagemaker.types.optimization_job_environment_variables.OptimizationJobEnvironmentVariables"
    ]
    """<p>Environment variables that override the default ones in the model container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelShardingConfig) -> dict:
    out: dict = {}
    if "image" in value:
        out["Image"] = value["image"]
    if "override_environment" in value:
        import capo_sagemaker.types.optimization_job_environment_variables

        out["OverrideEnvironment"] = (
            capo_sagemaker.types.optimization_job_environment_variables.serialize_aws_json_1_1(
                value["override_environment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelShardingConfig:
    out: ModelShardingConfig = {}  # type: ignore[typeddict-item]
    if "Image" in data:
        out["image"] = data["Image"]
    if "OverrideEnvironment" in data:
        import capo_sagemaker.types.optimization_job_environment_variables

        out["override_environment"] = (
            capo_sagemaker.types.optimization_job_environment_variables.deserialize_aws_json_1_1(
                data["OverrideEnvironment"]
            )
        )
    return out
