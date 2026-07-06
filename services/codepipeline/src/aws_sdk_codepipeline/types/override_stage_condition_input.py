"""Generated from Smithy shape ``com.amazonaws.codepipeline#OverrideStageConditionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.condition_type
    import aws_sdk_codepipeline.types.pipeline_execution_id
    import aws_sdk_codepipeline.types.pipeline_name
    import aws_sdk_codepipeline.types.stage_name


class OverrideStageConditionInput(TypedDict, closed=True):
    pipeline_name: "aws_sdk_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline with the stage that will override the condition.</p>"""
    stage_name: "aws_sdk_codepipeline.types.stage_name.StageName"
    """<p>The name of the stage for the override.</p>"""
    pipeline_execution_id: (
        "aws_sdk_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    )
    """<p>The ID of the pipeline execution for the override.</p>"""
    condition_type: "aws_sdk_codepipeline.types.condition_type.ConditionType"
    """<p>The type of condition to override for the stage, such as entry conditions, failure conditions, or success conditions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OverrideStageConditionInput) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    out["stageName"] = value["stage_name"]
    out["pipelineExecutionId"] = value["pipeline_execution_id"]
    import aws_sdk_codepipeline.types.condition_type

    out["conditionType"] = (
        aws_sdk_codepipeline.types.condition_type.serialize_aws_json_1_1(
            value["condition_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OverrideStageConditionInput:
    out: OverrideStageConditionInput = {}  # type: ignore[typeddict-item]
    if "pipelineName" in data:
        out["pipeline_name"] = data["pipelineName"]
    else:
        raise DeserializationError("OverrideStageConditionInput.pipeline_name required")
    if "stageName" in data:
        out["stage_name"] = data["stageName"]
    else:
        raise DeserializationError("OverrideStageConditionInput.stage_name required")
    if "pipelineExecutionId" in data:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    else:
        raise DeserializationError(
            "OverrideStageConditionInput.pipeline_execution_id required"
        )
    if "conditionType" in data:
        import aws_sdk_codepipeline.types.condition_type

        out["condition_type"] = (
            aws_sdk_codepipeline.types.condition_type.deserialize_aws_json_1_1(
                data["conditionType"]
            )
        )
    else:
        raise DeserializationError(
            "OverrideStageConditionInput.condition_type required"
        )
    return out
