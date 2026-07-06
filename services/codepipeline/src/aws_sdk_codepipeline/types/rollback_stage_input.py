"""Generated from Smithy shape ``com.amazonaws.codepipeline#RollbackStageInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.pipeline_execution_id
    import aws_sdk_codepipeline.types.pipeline_name
    import aws_sdk_codepipeline.types.stage_name


class RollbackStageInput(TypedDict, closed=True):
    pipeline_name: "aws_sdk_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline for which the stage will be rolled back. </p>"""
    stage_name: "aws_sdk_codepipeline.types.stage_name.StageName"
    """<p>The name of the stage in the pipeline to be rolled back. </p>"""
    target_pipeline_execution_id: (
        "aws_sdk_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    )
    """<p>The pipeline execution ID for the stage to be rolled back to. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RollbackStageInput) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    out["stageName"] = value["stage_name"]
    out["targetPipelineExecutionId"] = value["target_pipeline_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RollbackStageInput:
    out: RollbackStageInput = {}  # type: ignore[typeddict-item]
    if "pipelineName" in data:
        out["pipeline_name"] = data["pipelineName"]
    else:
        raise DeserializationError("RollbackStageInput.pipeline_name required")
    if "stageName" in data:
        out["stage_name"] = data["stageName"]
    else:
        raise DeserializationError("RollbackStageInput.stage_name required")
    if "targetPipelineExecutionId" in data:
        out["target_pipeline_execution_id"] = data["targetPipelineExecutionId"]
    else:
        raise DeserializationError(
            "RollbackStageInput.target_pipeline_execution_id required"
        )
    return out
