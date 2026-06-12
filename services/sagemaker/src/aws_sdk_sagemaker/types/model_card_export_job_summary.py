"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardExportJobSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.integer
    import aws_sdk_sagemaker.types.model_card_export_job_arn
    import aws_sdk_sagemaker.types.model_card_export_job_status
    import aws_sdk_sagemaker.types.timestamp


class ModelCardExportJobSummary(TypedDict):
    model_card_export_job_name: NotRequired[
        "aws_sdk_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the model card export job.</p>"""
    model_card_export_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.model_card_export_job_arn.ModelCardExportJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model card export job.</p>"""
    status: NotRequired[
        "aws_sdk_sagemaker.types.model_card_export_job_status.ModelCardExportJobStatus"
    ]
    """<p>The completion status of the model card export job.</p>"""
    model_card_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model card that the export job exports.</p>"""
    model_card_version: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The version of the model card that the export job exports.</p>"""
    created_at: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the model card export job was created.</p>"""
    last_modified_at: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the model card export job was last modified..</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCardExportJobSummary) -> dict:
    out: dict = {}
    if "model_card_export_job_name" in value:
        out["ModelCardExportJobName"] = value["model_card_export_job_name"]
    if "model_card_export_job_arn" in value:
        out["ModelCardExportJobArn"] = value["model_card_export_job_arn"]
    if "status" in value:
        import aws_sdk_sagemaker.types.model_card_export_job_status

        out["Status"] = (
            aws_sdk_sagemaker.types.model_card_export_job_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "model_card_name" in value:
        out["ModelCardName"] = value["model_card_name"]
    if "model_card_version" in value:
        out["ModelCardVersion"] = value["model_card_version"]
    if "created_at" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreatedAt"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "last_modified_at" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedAt"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelCardExportJobSummary:
    out: ModelCardExportJobSummary = {}  # type: ignore[typeddict-item]
    if "ModelCardExportJobName" in data:
        out["model_card_export_job_name"] = data["ModelCardExportJobName"]
    if "ModelCardExportJobArn" in data:
        out["model_card_export_job_arn"] = data["ModelCardExportJobArn"]
    if "Status" in data:
        import aws_sdk_sagemaker.types.model_card_export_job_status

        out["status"] = (
            aws_sdk_sagemaker.types.model_card_export_job_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "ModelCardName" in data:
        out["model_card_name"] = data["ModelCardName"]
    if "ModelCardVersion" in data:
        out["model_card_version"] = data["ModelCardVersion"]
    if "CreatedAt" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["created_at"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if "LastModifiedAt" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_at"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedAt"]
            )
        )
    return out
