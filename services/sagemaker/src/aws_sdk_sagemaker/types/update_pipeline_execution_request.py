"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdatePipelineExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.parallelism_configuration
    import aws_sdk_sagemaker.types.pipeline_execution_arn
    import aws_sdk_sagemaker.types.pipeline_execution_description
    import aws_sdk_sagemaker.types.pipeline_execution_name


class UpdatePipelineExecutionRequest(TypedDict, closed=True):
    pipeline_execution_arn: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_execution_arn.PipelineExecutionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the pipeline execution.</p>"""
    pipeline_execution_description: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_execution_description.PipelineExecutionDescription"
    ]
    """<p>The description of the pipeline execution.</p>"""
    pipeline_execution_display_name: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_execution_name.PipelineExecutionName"
    ]
    """<p>The display name of the pipeline execution.</p>"""
    parallelism_configuration: NotRequired[
        "aws_sdk_sagemaker.types.parallelism_configuration.ParallelismConfiguration"
    ]
    """<p>This configuration, if specified, overrides the parallelism configuration of the parent pipeline for this specific run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePipelineExecutionRequest) -> dict:
    out: dict = {}
    if "pipeline_execution_arn" in value:
        out["PipelineExecutionArn"] = value["pipeline_execution_arn"]
    if "pipeline_execution_description" in value:
        out["PipelineExecutionDescription"] = value["pipeline_execution_description"]
    if "pipeline_execution_display_name" in value:
        out["PipelineExecutionDisplayName"] = value["pipeline_execution_display_name"]
    if "parallelism_configuration" in value:
        import aws_sdk_sagemaker.types.parallelism_configuration

        out["ParallelismConfiguration"] = (
            aws_sdk_sagemaker.types.parallelism_configuration.serialize_aws_json_1_1(
                value["parallelism_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePipelineExecutionRequest:
    out: UpdatePipelineExecutionRequest = {}  # type: ignore[typeddict-item]
    if "PipelineExecutionArn" in data:
        out["pipeline_execution_arn"] = data["PipelineExecutionArn"]
    if "PipelineExecutionDescription" in data:
        out["pipeline_execution_description"] = data["PipelineExecutionDescription"]
    if "PipelineExecutionDisplayName" in data:
        out["pipeline_execution_display_name"] = data["PipelineExecutionDisplayName"]
    if "ParallelismConfiguration" in data:
        import aws_sdk_sagemaker.types.parallelism_configuration

        out["parallelism_configuration"] = (
            aws_sdk_sagemaker.types.parallelism_configuration.deserialize_aws_json_1_1(
                data["ParallelismConfiguration"]
            )
        )
    return out
