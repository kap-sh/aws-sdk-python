"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelInfrastructureConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_infrastructure_type
    import aws_sdk_sagemaker.types.real_time_inference_config


class ModelInfrastructureConfig(TypedDict):
    infrastructure_type: NotRequired[
        "aws_sdk_sagemaker.types.model_infrastructure_type.ModelInfrastructureType"
    ]
    """<p>The inference option to which to deploy your model. Possible values are the following:</p> <ul> <li> <p> <code>RealTime</code>: Deploy to real-time inference.</p> </li> </ul>"""
    real_time_inference_config: NotRequired[
        "aws_sdk_sagemaker.types.real_time_inference_config.RealTimeInferenceConfig"
    ]
    """<p>The infrastructure configuration for deploying the model to real-time inference.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelInfrastructureConfig) -> dict:
    out: dict = {}
    if "infrastructure_type" in value:
        import aws_sdk_sagemaker.types.model_infrastructure_type

        out["InfrastructureType"] = (
            aws_sdk_sagemaker.types.model_infrastructure_type.serialize_aws_json_1_1(
                value["infrastructure_type"]
            )
        )
    if "real_time_inference_config" in value:
        import aws_sdk_sagemaker.types.real_time_inference_config

        out["RealTimeInferenceConfig"] = (
            aws_sdk_sagemaker.types.real_time_inference_config.serialize_aws_json_1_1(
                value["real_time_inference_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelInfrastructureConfig:
    out: ModelInfrastructureConfig = {}  # type: ignore[typeddict-item]
    if "InfrastructureType" in data:
        import aws_sdk_sagemaker.types.model_infrastructure_type

        out["infrastructure_type"] = (
            aws_sdk_sagemaker.types.model_infrastructure_type.deserialize_aws_json_1_1(
                data["InfrastructureType"]
            )
        )
    if "RealTimeInferenceConfig" in data:
        import aws_sdk_sagemaker.types.real_time_inference_config

        out["real_time_inference_config"] = (
            aws_sdk_sagemaker.types.real_time_inference_config.deserialize_aws_json_1_1(
                data["RealTimeInferenceConfig"]
            )
        )
    return out
