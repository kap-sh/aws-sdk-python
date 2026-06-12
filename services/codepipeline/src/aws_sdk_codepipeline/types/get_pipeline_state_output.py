"""Generated from Smithy shape ``com.amazonaws.codepipeline#GetPipelineStateOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.pipeline_name
    import aws_sdk_codepipeline.types.pipeline_version
    import aws_sdk_codepipeline.types.stage_state_list
    import aws_sdk_codepipeline.types.timestamp


class GetPipelineStateOutput(TypedDict):
    pipeline_name: NotRequired["aws_sdk_codepipeline.types.pipeline_name.PipelineName"]
    """<p>The name of the pipeline for which you want to get the state.</p>"""
    pipeline_version: NotRequired[
        "aws_sdk_codepipeline.types.pipeline_version.PipelineVersion"
    ]
    """<p>The version number of the pipeline.</p> <note> <p>A newly created pipeline is always assigned a version number of <code>1</code>.</p> </note>"""
    stage_states: NotRequired[
        "aws_sdk_codepipeline.types.stage_state_list.StageStateList"
    ]
    """<p>A list of the pipeline stage output information, including stage name, state, most recent run details, whether the stage is disabled, and other data.</p>"""
    created: NotRequired["aws_sdk_codepipeline.types.timestamp.Timestamp"]
    """<p>The date and time the pipeline was created, in timestamp format.</p>"""
    updated: NotRequired["aws_sdk_codepipeline.types.timestamp.Timestamp"]
    """<p>The date and time the pipeline was last updated, in timestamp format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPipelineStateOutput) -> dict:
    out: dict = {}
    if "pipeline_name" in value:
        out["pipelineName"] = value["pipeline_name"]
    if "pipeline_version" in value:
        out["pipelineVersion"] = value["pipeline_version"]
    if "stage_states" in value:
        import aws_sdk_codepipeline.types.stage_state_list

        out["stageStates"] = (
            aws_sdk_codepipeline.types.stage_state_list.serialize_aws_json_1_1(
                value["stage_states"]
            )
        )
    if "created" in value:
        import aws_sdk_codepipeline.types.timestamp

        out["created"] = aws_sdk_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["created"]
        )
    if "updated" in value:
        import aws_sdk_codepipeline.types.timestamp

        out["updated"] = aws_sdk_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["updated"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPipelineStateOutput:
    out: GetPipelineStateOutput = {}  # type: ignore[typeddict-item]
    if "pipelineName" in data:
        out["pipeline_name"] = data["pipelineName"]
    if "pipelineVersion" in data:
        out["pipeline_version"] = data["pipelineVersion"]
    if "stageStates" in data:
        import aws_sdk_codepipeline.types.stage_state_list

        out["stage_states"] = (
            aws_sdk_codepipeline.types.stage_state_list.deserialize_aws_json_1_1(
                data["stageStates"]
            )
        )
    if "created" in data:
        import aws_sdk_codepipeline.types.timestamp

        out["created"] = aws_sdk_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["created"]
        )
    if "updated" in data:
        import aws_sdk_codepipeline.types.timestamp

        out["updated"] = aws_sdk_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["updated"]
        )
    return out
