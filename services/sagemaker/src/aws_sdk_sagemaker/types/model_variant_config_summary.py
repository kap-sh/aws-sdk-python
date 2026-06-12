"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelVariantConfigSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_infrastructure_config
    import aws_sdk_sagemaker.types.model_name
    import aws_sdk_sagemaker.types.model_variant_name
    import aws_sdk_sagemaker.types.model_variant_status


class ModelVariantConfigSummary(TypedDict):
    model_name: NotRequired["aws_sdk_sagemaker.types.model_name.ModelName"]
    """<p>The name of the Amazon SageMaker Model entity.</p>"""
    variant_name: NotRequired[
        "aws_sdk_sagemaker.types.model_variant_name.ModelVariantName"
    ]
    """<p>The name of the variant.</p>"""
    infrastructure_config: NotRequired[
        "aws_sdk_sagemaker.types.model_infrastructure_config.ModelInfrastructureConfig"
    ]
    """<p>The configuration of the infrastructure that the model has been deployed to.</p>"""
    status: NotRequired[
        "aws_sdk_sagemaker.types.model_variant_status.ModelVariantStatus"
    ]
    """<p>The status of deployment for the model variant on the hosted inference endpoint.</p> <ul> <li> <p> <code>Creating</code> - Amazon SageMaker is preparing the model variant on the hosted inference endpoint. </p> </li> <li> <p> <code>InService</code> - The model variant is running on the hosted inference endpoint. </p> </li> <li> <p> <code>Updating</code> - Amazon SageMaker is updating the model variant on the hosted inference endpoint. </p> </li> <li> <p> <code>Deleting</code> - Amazon SageMaker is deleting the model variant on the hosted inference endpoint. </p> </li> <li> <p> <code>Deleted</code> - The model variant has been deleted on the hosted inference endpoint. This can only happen after stopping the experiment. </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelVariantConfigSummary) -> dict:
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
    if "status" in value:
        import aws_sdk_sagemaker.types.model_variant_status

        out["Status"] = (
            aws_sdk_sagemaker.types.model_variant_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelVariantConfigSummary:
    out: ModelVariantConfigSummary = {}  # type: ignore[typeddict-item]
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
    if "Status" in data:
        import aws_sdk_sagemaker.types.model_variant_status

        out["status"] = (
            aws_sdk_sagemaker.types.model_variant_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out
