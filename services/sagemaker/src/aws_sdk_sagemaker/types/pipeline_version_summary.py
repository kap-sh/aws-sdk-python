"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.pipeline_arn
    import aws_sdk_sagemaker.types.pipeline_execution_arn
    import aws_sdk_sagemaker.types.pipeline_version_description
    import aws_sdk_sagemaker.types.pipeline_version_id
    import aws_sdk_sagemaker.types.pipeline_version_name
    import aws_sdk_sagemaker.types.timestamp


class PipelineVersionSummary(TypedDict, closed=True):
    pipeline_arn: NotRequired["aws_sdk_sagemaker.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the pipeline.</p>"""
    pipeline_version_id: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_version_id.PipelineVersionId"
    ]
    """<p>The ID of the pipeline version.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The creation time of the pipeline version.</p>"""
    pipeline_version_description: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_version_description.PipelineVersionDescription"
    ]
    """<p>The description of the pipeline version.</p>"""
    pipeline_version_display_name: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_version_name.PipelineVersionName"
    ]
    """<p>The display name of the pipeline version.</p>"""
    last_execution_pipeline_execution_arn: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_execution_arn.PipelineExecutionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the most recent pipeline execution created from this pipeline version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineVersionSummary) -> dict:
    out: dict = {}
    if "pipeline_arn" in value:
        out["PipelineArn"] = value["pipeline_arn"]
    if "pipeline_version_id" in value:
        out["PipelineVersionId"] = value["pipeline_version_id"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "pipeline_version_description" in value:
        out["PipelineVersionDescription"] = value["pipeline_version_description"]
    if "pipeline_version_display_name" in value:
        out["PipelineVersionDisplayName"] = value["pipeline_version_display_name"]
    if "last_execution_pipeline_execution_arn" in value:
        out["LastExecutionPipelineExecutionArn"] = value[
            "last_execution_pipeline_execution_arn"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineVersionSummary:
    out: PipelineVersionSummary = {}  # type: ignore[typeddict-item]
    if "PipelineArn" in data:
        out["pipeline_arn"] = data["PipelineArn"]
    if "PipelineVersionId" in data:
        out["pipeline_version_id"] = data["PipelineVersionId"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "PipelineVersionDescription" in data:
        out["pipeline_version_description"] = data["PipelineVersionDescription"]
    if "PipelineVersionDisplayName" in data:
        out["pipeline_version_display_name"] = data["PipelineVersionDisplayName"]
    if "LastExecutionPipelineExecutionArn" in data:
        out["last_execution_pipeline_execution_arn"] = data[
            "LastExecutionPipelineExecutionArn"
        ]
    return out
