"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelVariantConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_infrastructure_config
    import aws_sdk_sagemaker.types.model_name
    import aws_sdk_sagemaker.types.model_variant_name


class ModelVariantConfig(TypedDict):
    model_name: NotRequired["aws_sdk_sagemaker.types.model_name.ModelName"]
    """<p>The name of the Amazon SageMaker Model entity.</p>"""
    variant_name: NotRequired[
        "aws_sdk_sagemaker.types.model_variant_name.ModelVariantName"
    ]
    """<p>The name of the variant.</p>"""
    infrastructure_config: NotRequired[
        "aws_sdk_sagemaker.types.model_infrastructure_config.ModelInfrastructureConfig"
    ]
    """<p>The configuration for the infrastructure that the model will be deployed to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelVariantConfig) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "variant_name" in value:
        out["VariantName"] = value["variant_name"]
    if "infrastructure_config" in value:
        import aws_sdk_sagemaker.types.model_infrastructure_config

        out["InfrastructureConfig"] = (
            aws_sdk_sagemaker.types.model_infrastructure_config.serialize_aws_json_1_1(
                value["infrastructure_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelVariantConfig:
    out: ModelVariantConfig = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "VariantName" in data:
        out["variant_name"] = data["VariantName"]
    if "InfrastructureConfig" in data:
        import aws_sdk_sagemaker.types.model_infrastructure_config

        out["infrastructure_config"] = (
            aws_sdk_sagemaker.types.model_infrastructure_config.deserialize_aws_json_1_1(
                data["InfrastructureConfig"]
            )
        )
    return out
