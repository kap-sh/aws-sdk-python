"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelInfrastructureConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.model_infrastructure_type
    import capo_sagemaker.types.real_time_inference_config


class ModelInfrastructureConfig(TypedDict, closed=True):
    infrastructure_type: NotRequired[
        "capo_sagemaker.types.model_infrastructure_type.ModelInfrastructureType"
    ]
    """<p>The inference option to which to deploy your model. Possible values are the following:</p> <ul> <li> <p> <code>RealTime</code>: Deploy to real-time inference.</p> </li> </ul>"""
    real_time_inference_config: NotRequired[
        "capo_sagemaker.types.real_time_inference_config.RealTimeInferenceConfig"
    ]
    """<p>The infrastructure configuration for deploying the model to real-time inference.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelInfrastructureConfig) -> dict:
    out: dict = {}
    if "infrastructure_type" in value:
        import capo_sagemaker.types.model_infrastructure_type

        out["InfrastructureType"] = (
            capo_sagemaker.types.model_infrastructure_type.serialize_aws_json_1_1(
                value["infrastructure_type"]
            )
        )
    if "real_time_inference_config" in value:
        import capo_sagemaker.types.real_time_inference_config

        out["RealTimeInferenceConfig"] = (
            capo_sagemaker.types.real_time_inference_config.serialize_aws_json_1_1(
                value["real_time_inference_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelInfrastructureConfig:
    out: ModelInfrastructureConfig = {}  # type: ignore[typeddict-item]
    if "InfrastructureType" in data:
        import capo_sagemaker.types.model_infrastructure_type

        out["infrastructure_type"] = (
            capo_sagemaker.types.model_infrastructure_type.deserialize_aws_json_1_1(
                data["InfrastructureType"]
            )
        )
    if "RealTimeInferenceConfig" in data:
        import capo_sagemaker.types.real_time_inference_config

        out["real_time_inference_config"] = (
            capo_sagemaker.types.real_time_inference_config.deserialize_aws_json_1_1(
                data["RealTimeInferenceConfig"]
            )
        )
    return out
