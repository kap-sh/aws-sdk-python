"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageExecution``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.execution_type
    import aws_sdk_codepipeline.types.pipeline_execution_id
    import aws_sdk_codepipeline.types.stage_execution_status


class StageExecution(TypedDict):
    pipeline_execution_id: (
        "aws_sdk_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    )
    """<p>The ID of the pipeline execution associated with the stage.</p>"""
    status: "aws_sdk_codepipeline.types.stage_execution_status.StageExecutionStatus"
    """<p>The status of the stage, or for a completed stage, the last status of the stage.</p> <note> <p>A status of cancelled means that the pipeline’s definition was updated before the stage execution could be completed.</p> </note>"""
    type: NotRequired["aws_sdk_codepipeline.types.execution_type.ExecutionType"]
    """<p>The type of pipeline execution for the stage, such as a rollback pipeline execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageExecution) -> dict:
    out: dict = {}
    out["pipelineExecutionId"] = value["pipeline_execution_id"]
    import aws_sdk_codepipeline.types.stage_execution_status

    out["status"] = (
        aws_sdk_codepipeline.types.stage_execution_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "type" in value:
        import aws_sdk_codepipeline.types.execution_type

        out["type"] = aws_sdk_codepipeline.types.execution_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StageExecution:
    out: StageExecution = {}  # type: ignore[typeddict-item]
    if "pipelineExecutionId" in data:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    else:
        raise DeserializationError("StageExecution.pipeline_execution_id required")
    if "status" in data:
        import aws_sdk_codepipeline.types.stage_execution_status

        out["status"] = (
            aws_sdk_codepipeline.types.stage_execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        raise DeserializationError("StageExecution.status required")
    if "type" in data:
        import aws_sdk_codepipeline.types.execution_type

        out["type"] = (
            aws_sdk_codepipeline.types.execution_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    return out
