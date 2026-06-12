"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineContext``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_context
    import aws_sdk_codepipeline.types.pipeline_arn
    import aws_sdk_codepipeline.types.pipeline_execution_id
    import aws_sdk_codepipeline.types.pipeline_name
    import aws_sdk_codepipeline.types.stage_context


class PipelineContext(TypedDict):
    pipeline_name: NotRequired["aws_sdk_codepipeline.types.pipeline_name.PipelineName"]
    """<p>The name of the pipeline. This is a user-specified value. Pipeline names must be unique across all pipeline names under an Amazon Web Services account.</p>"""
    stage: NotRequired["aws_sdk_codepipeline.types.stage_context.StageContext"]
    """<p>The stage of the pipeline.</p>"""
    action: NotRequired["aws_sdk_codepipeline.types.action_context.ActionContext"]
    """<p>The context of an action to a job worker in the stage of a pipeline.</p>"""
    pipeline_arn: NotRequired["aws_sdk_codepipeline.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the pipeline.</p>"""
    pipeline_execution_id: NotRequired[
        "aws_sdk_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    ]
    """<p>The execution ID of the pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineContext) -> dict:
    out: dict = {}
    if "pipeline_name" in value:
        out["pipelineName"] = value["pipeline_name"]
    if "stage" in value:
        import aws_sdk_codepipeline.types.stage_context

        out["stage"] = aws_sdk_codepipeline.types.stage_context.serialize_aws_json_1_1(
            value["stage"]
        )
    if "action" in value:
        import aws_sdk_codepipeline.types.action_context

        out["action"] = (
            aws_sdk_codepipeline.types.action_context.serialize_aws_json_1_1(
                value["action"]
            )
        )
    if "pipeline_arn" in value:
        out["pipelineArn"] = value["pipeline_arn"]
    if "pipeline_execution_id" in value:
        out["pipelineExecutionId"] = value["pipeline_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineContext:
    out: PipelineContext = {}  # type: ignore[typeddict-item]
    if "pipelineName" in data:
        out["pipeline_name"] = data["pipelineName"]
    if "stage" in data:
        import aws_sdk_codepipeline.types.stage_context

        out["stage"] = (
            aws_sdk_codepipeline.types.stage_context.deserialize_aws_json_1_1(
                data["stage"]
            )
        )
    if "action" in data:
        import aws_sdk_codepipeline.types.action_context

        out["action"] = (
            aws_sdk_codepipeline.types.action_context.deserialize_aws_json_1_1(
                data["action"]
            )
        )
    if "pipelineArn" in data:
        out["pipeline_arn"] = data["pipelineArn"]
    if "pipelineExecutionId" in data:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    return out
