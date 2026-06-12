"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateModelCardExportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.integer
    import aws_sdk_sagemaker.types.model_card_export_output_config
    import aws_sdk_sagemaker.types.model_card_name_or_arn


class CreateModelCardExportJobRequest(TypedDict):
    model_card_name: NotRequired[
        "aws_sdk_sagemaker.types.model_card_name_or_arn.ModelCardNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the model card to export.</p>"""
    model_card_version: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The version of the model card to export. If a version is not provided, then the latest version of the model card is exported.</p>"""
    model_card_export_job_name: NotRequired[
        "aws_sdk_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the model card export job.</p>"""
    output_config: NotRequired[
        "aws_sdk_sagemaker.types.model_card_export_output_config.ModelCardExportOutputConfig"
    ]
    """<p>The model card output configuration that specifies the Amazon S3 path for exporting.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateModelCardExportJobRequest) -> dict:
    out: dict = {}
    if "model_card_name" in value:
        out["ModelCardName"] = value["model_card_name"]
    if "model_card_version" in value:
        out["ModelCardVersion"] = value["model_card_version"]
    if "model_card_export_job_name" in value:
        out["ModelCardExportJobName"] = value["model_card_export_job_name"]
    if "output_config" in value:
        import aws_sdk_sagemaker.types.model_card_export_output_config

        out["OutputConfig"] = (
            aws_sdk_sagemaker.types.model_card_export_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateModelCardExportJobRequest:
    out: CreateModelCardExportJobRequest = {}  # type: ignore[typeddict-item]
    if "ModelCardName" in data:
        out["model_card_name"] = data["ModelCardName"]
    if "ModelCardVersion" in data:
        out["model_card_version"] = data["ModelCardVersion"]
    if "ModelCardExportJobName" in data:
        out["model_card_export_job_name"] = data["ModelCardExportJobName"]
    if "OutputConfig" in data:
        import aws_sdk_sagemaker.types.model_card_export_output_config

        out["output_config"] = (
            aws_sdk_sagemaker.types.model_card_export_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    return out
