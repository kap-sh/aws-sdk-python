"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeModelCardExportJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.integer
    import aws_sdk_sagemaker.types.model_card_export_artifacts
    import aws_sdk_sagemaker.types.model_card_export_job_arn
    import aws_sdk_sagemaker.types.model_card_export_job_status
    import aws_sdk_sagemaker.types.model_card_export_output_config
    import aws_sdk_sagemaker.types.timestamp


class DescribeModelCardExportJobResponse(TypedDict):
    model_card_export_job_name: NotRequired[
        "aws_sdk_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The name of the model card export job to describe.</p>"""
    model_card_export_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.model_card_export_job_arn.ModelCardExportJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model card export job.</p>"""
    status: NotRequired[
        "aws_sdk_sagemaker.types.model_card_export_job_status.ModelCardExportJobStatus"
    ]
    """<p>The completion status of the model card export job.</p> <ul> <li> <p> <code>InProgress</code>: The model card export job is in progress.</p> </li> <li> <p> <code>Completed</code>: The model card export job is complete.</p> </li> <li> <p> <code>Failed</code>: The model card export job failed. To see the reason for the failure, see the <code>FailureReason</code> field in the response to a <code>DescribeModelCardExportJob</code> call.</p> </li> </ul>"""
    model_card_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name or Amazon Resource Name (ARN) of the model card that the model export job exports.</p>"""
    model_card_version: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The version of the model card that the model export job exports.</p>"""
    output_config: NotRequired[
        "aws_sdk_sagemaker.types.model_card_export_output_config.ModelCardExportOutputConfig"
    ]
    """<p>The export output details for the model card.</p>"""
    created_at: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the model export job was created.</p>"""
    last_modified_at: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the model export job was last modified.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>The failure reason if the model export job fails.</p>"""
    export_artifacts: NotRequired[
        "aws_sdk_sagemaker.types.model_card_export_artifacts.ModelCardExportArtifacts"
    ]
    """<p>The exported model card artifacts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeModelCardExportJobResponse) -> dict:
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
    if "output_config" in value:
        import aws_sdk_sagemaker.types.model_card_export_output_config

        out["OutputConfig"] = (
            aws_sdk_sagemaker.types.model_card_export_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
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
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "export_artifacts" in value:
        import aws_sdk_sagemaker.types.model_card_export_artifacts

        out["ExportArtifacts"] = (
            aws_sdk_sagemaker.types.model_card_export_artifacts.serialize_aws_json_1_1(
                value["export_artifacts"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeModelCardExportJobResponse:
    out: DescribeModelCardExportJobResponse = {}  # type: ignore[typeddict-item]
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
    if "OutputConfig" in data:
        import aws_sdk_sagemaker.types.model_card_export_output_config

        out["output_config"] = (
            aws_sdk_sagemaker.types.model_card_export_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
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
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "ExportArtifacts" in data:
        import aws_sdk_sagemaker.types.model_card_export_artifacts

        out["export_artifacts"] = (
            aws_sdk_sagemaker.types.model_card_export_artifacts.deserialize_aws_json_1_1(
                data["ExportArtifacts"]
            )
        )
    return out
