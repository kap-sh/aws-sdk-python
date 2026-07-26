"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.pipeline_arn
    import capo_sagemaker.types.pipeline_description
    import capo_sagemaker.types.pipeline_name
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.timestamp


class PipelineSummary(TypedDict, closed=True):
    pipeline_arn: NotRequired["capo_sagemaker.types.pipeline_arn.PipelineArn"]
    """<p> The Amazon Resource Name (ARN) of the pipeline.</p>"""
    pipeline_name: NotRequired["capo_sagemaker.types.pipeline_name.PipelineName"]
    """<p>The name of the pipeline.</p>"""
    pipeline_display_name: NotRequired[
        "capo_sagemaker.types.pipeline_name.PipelineName"
    ]
    """<p>The display name of the pipeline.</p>"""
    pipeline_description: NotRequired[
        "capo_sagemaker.types.pipeline_description.PipelineDescription"
    ]
    """<p>The description of the pipeline.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) that the pipeline used to execute.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The creation time of the pipeline.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time that the pipeline was last modified.</p>"""
    last_execution_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The last time that a pipeline execution began.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineSummary) -> dict:
    out: dict = {}
    if "pipeline_arn" in value:
        out["PipelineArn"] = value["pipeline_arn"]
    if "pipeline_name" in value:
        out["PipelineName"] = value["pipeline_name"]
    if "pipeline_display_name" in value:
        out["PipelineDisplayName"] = value["pipeline_display_name"]
    if "pipeline_description" in value:
        out["PipelineDescription"] = value["pipeline_description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "last_execution_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastExecutionTime"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_execution_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineSummary:
    out: PipelineSummary = {}  # type: ignore[typeddict-item]
    if "PipelineArn" in data:
        out["pipeline_arn"] = data["PipelineArn"]
    if "PipelineName" in data:
        out["pipeline_name"] = data["PipelineName"]
    if "PipelineDisplayName" in data:
        out["pipeline_display_name"] = data["PipelineDisplayName"]
    if "PipelineDescription" in data:
        out["pipeline_description"] = data["PipelineDescription"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastExecutionTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_execution_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastExecutionTime"]
            )
        )
    return out
