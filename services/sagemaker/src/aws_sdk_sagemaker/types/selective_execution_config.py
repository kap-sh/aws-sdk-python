"""Generated from Smithy shape ``com.amazonaws.sagemaker#SelectiveExecutionConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.pipeline_execution_arn
    import aws_sdk_sagemaker.types.selected_step_list


class SelectiveExecutionConfig(TypedDict):
    source_pipeline_execution_arn: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_execution_arn.PipelineExecutionArn"
    ]
    """<p>The ARN from a reference execution of the current pipeline. Used to copy input collaterals needed for the selected steps to run. The execution status of the pipeline can be either <code>Failed</code> or <code>Success</code>.</p> <p>This field is required if the steps you specify for <code>SelectedSteps</code> depend on output collaterals from any non-specified pipeline steps. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-selective-ex.html\">Selective Execution for Pipeline Steps</a>.</p>"""
    selected_steps: NotRequired[
        "aws_sdk_sagemaker.types.selected_step_list.SelectedStepList"
    ]
    """<p>A list of pipeline steps to run. All step(s) in all path(s) between two selected steps should be included.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelectiveExecutionConfig) -> dict:
    out: dict = {}
    if "source_pipeline_execution_arn" in value:
        out["SourcePipelineExecutionArn"] = value["source_pipeline_execution_arn"]
    if "selected_steps" in value:
        import aws_sdk_sagemaker.types.selected_step_list

        out["SelectedSteps"] = (
            aws_sdk_sagemaker.types.selected_step_list.serialize_aws_json_1_1(
                value["selected_steps"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SelectiveExecutionConfig:
    out: SelectiveExecutionConfig = {}  # type: ignore[typeddict-item]
    if "SourcePipelineExecutionArn" in data:
        out["source_pipeline_execution_arn"] = data["SourcePipelineExecutionArn"]
    if "SelectedSteps" in data:
        import aws_sdk_sagemaker.types.selected_step_list

        out["selected_steps"] = (
            aws_sdk_sagemaker.types.selected_step_list.deserialize_aws_json_1_1(
                data["SelectedSteps"]
            )
        )
    return out
