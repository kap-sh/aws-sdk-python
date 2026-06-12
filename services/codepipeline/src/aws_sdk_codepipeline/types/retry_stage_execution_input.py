"""Generated from Smithy shape ``com.amazonaws.codepipeline#RetryStageExecutionInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.pipeline_execution_id
    import aws_sdk_codepipeline.types.pipeline_name
    import aws_sdk_codepipeline.types.stage_name
    import aws_sdk_codepipeline.types.stage_retry_mode


class RetryStageExecutionInput(TypedDict):
    pipeline_name: "aws_sdk_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline that contains the failed stage.</p>"""
    stage_name: "aws_sdk_codepipeline.types.stage_name.StageName"
    """<p>The name of the failed stage to be retried.</p>"""
    pipeline_execution_id: (
        "aws_sdk_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    )
    """<p>The ID of the pipeline execution in the failed stage to be retried. Use the <a>GetPipelineState</a> action to retrieve the current pipelineExecutionId of the failed stage</p>"""
    retry_mode: "aws_sdk_codepipeline.types.stage_retry_mode.StageRetryMode"
    """<p>The scope of the retry attempt.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetryStageExecutionInput) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    out["stageName"] = value["stage_name"]
    out["pipelineExecutionId"] = value["pipeline_execution_id"]
    import aws_sdk_codepipeline.types.stage_retry_mode

    out["retryMode"] = (
        aws_sdk_codepipeline.types.stage_retry_mode.serialize_aws_json_1_1(
            value["retry_mode"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RetryStageExecutionInput:
    out: RetryStageExecutionInput = {}  # type: ignore[typeddict-item]
    if "pipelineName" in data:
        out["pipeline_name"] = data["pipelineName"]
    else:
        raise DeserializationError("RetryStageExecutionInput.pipeline_name required")
    if "stageName" in data:
        out["stage_name"] = data["stageName"]
    else:
        raise DeserializationError("RetryStageExecutionInput.stage_name required")
    if "pipelineExecutionId" in data:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    else:
        raise DeserializationError(
            "RetryStageExecutionInput.pipeline_execution_id required"
        )
    if "retryMode" in data:
        import aws_sdk_codepipeline.types.stage_retry_mode

        out["retry_mode"] = (
            aws_sdk_codepipeline.types.stage_retry_mode.deserialize_aws_json_1_1(
                data["retryMode"]
            )
        )
    else:
        raise DeserializationError("RetryStageExecutionInput.retry_mode required")
    return out
