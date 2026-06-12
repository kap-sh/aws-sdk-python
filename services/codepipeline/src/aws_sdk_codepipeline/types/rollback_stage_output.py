"""Generated from Smithy shape ``com.amazonaws.codepipeline#RollbackStageOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.pipeline_execution_id


class RollbackStageOutput(TypedDict):
    pipeline_execution_id: (
        "aws_sdk_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    )
    """<p>The execution ID of the pipeline execution for the stage that has been rolled back.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RollbackStageOutput) -> dict:
    out: dict = {}
    out["pipelineExecutionId"] = value["pipeline_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RollbackStageOutput:
    out: RollbackStageOutput = {}  # type: ignore[typeddict-item]
    if "pipelineExecutionId" in data:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    else:
        raise DeserializationError("RollbackStageOutput.pipeline_execution_id required")
    return out
