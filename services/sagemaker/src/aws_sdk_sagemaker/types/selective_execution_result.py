"""Generated from Smithy shape ``com.amazonaws.sagemaker#SelectiveExecutionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.pipeline_execution_arn


class SelectiveExecutionResult(TypedDict):
    source_pipeline_execution_arn: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_execution_arn.PipelineExecutionArn"
    ]
    """<p>The ARN from an execution of the current pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelectiveExecutionResult) -> dict:
    out: dict = {}
    if "source_pipeline_execution_arn" in value:
        out["SourcePipelineExecutionArn"] = value["source_pipeline_execution_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SelectiveExecutionResult:
    out: SelectiveExecutionResult = {}  # type: ignore[typeddict-item]
    if "SourcePipelineExecutionArn" in data:
        out["source_pipeline_execution_arn"] = data["SourcePipelineExecutionArn"]
    return out
