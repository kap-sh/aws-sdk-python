"""Generated from Smithy shape ``com.amazonaws.codepipeline#GetPipelineExecutionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.pipeline_execution


class GetPipelineExecutionOutput(TypedDict, closed=True):
    pipeline_execution: NotRequired[
        "aws_sdk_codepipeline.types.pipeline_execution.PipelineExecution"
    ]
    """<p>Represents information about the execution of a pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPipelineExecutionOutput) -> dict:
    out: dict = {}
    if "pipeline_execution" in value:
        import aws_sdk_codepipeline.types.pipeline_execution

        out["pipelineExecution"] = (
            aws_sdk_codepipeline.types.pipeline_execution.serialize_aws_json_1_1(
                value["pipeline_execution"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPipelineExecutionOutput:
    out: GetPipelineExecutionOutput = {}  # type: ignore[typeddict-item]
    if "pipelineExecution" in data:
        import aws_sdk_codepipeline.types.pipeline_execution

        out["pipeline_execution"] = (
            aws_sdk_codepipeline.types.pipeline_execution.deserialize_aws_json_1_1(
                data["pipelineExecution"]
            )
        )
    return out
