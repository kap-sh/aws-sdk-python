"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionExecutionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.action_execution_id
    import capo_codepipeline.types.action_execution_input
    import capo_codepipeline.types.action_execution_output
    import capo_codepipeline.types.action_execution_status
    import capo_codepipeline.types.action_name
    import capo_codepipeline.types.last_updated_by
    import capo_codepipeline.types.pipeline_execution_id
    import capo_codepipeline.types.pipeline_version
    import capo_codepipeline.types.stage_name
    import capo_codepipeline.types.timestamp


class ActionExecutionDetail(TypedDict, closed=True):
    pipeline_execution_id: NotRequired[
        "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    ]
    """<p>The pipeline execution ID for the action execution.</p>"""
    action_execution_id: NotRequired[
        "capo_codepipeline.types.action_execution_id.ActionExecutionId"
    ]
    """<p>The action execution ID.</p>"""
    pipeline_version: NotRequired[
        "capo_codepipeline.types.pipeline_version.PipelineVersion"
    ]
    """<p>The version of the pipeline where the action was run.</p>"""
    stage_name: NotRequired["capo_codepipeline.types.stage_name.StageName"]
    """<p>The name of the stage that contains the action.</p>"""
    action_name: NotRequired["capo_codepipeline.types.action_name.ActionName"]
    """<p>The name of the action.</p>"""
    start_time: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The start time of the action execution.</p>"""
    last_update_time: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The last update time of the action execution.</p>"""
    updated_by: NotRequired["capo_codepipeline.types.last_updated_by.LastUpdatedBy"]
    """<p>The ARN of the user who changed the pipeline execution details.</p>"""
    status: NotRequired[
        "capo_codepipeline.types.action_execution_status.ActionExecutionStatus"
    ]
    """<p> The status of the action execution. Status categories are <code>InProgress</code>, <code>Succeeded</code>, and <code>Failed</code>.</p>"""
    input: NotRequired[
        "capo_codepipeline.types.action_execution_input.ActionExecutionInput"
    ]
    """<p>Input details for the action execution, such as role ARN, Region, and input artifacts.</p>"""
    output: NotRequired[
        "capo_codepipeline.types.action_execution_output.ActionExecutionOutput"
    ]
    """<p>Output details for the action execution, such as the action execution result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionExecutionDetail) -> dict:
    out: dict = {}
    if "pipeline_execution_id" in value:
        out["pipelineExecutionId"] = value["pipeline_execution_id"]
    if "action_execution_id" in value:
        out["actionExecutionId"] = value["action_execution_id"]
    if "pipeline_version" in value:
        out["pipelineVersion"] = value["pipeline_version"]
    if "stage_name" in value:
        out["stageName"] = value["stage_name"]
    if "action_name" in value:
        out["actionName"] = value["action_name"]
    if "start_time" in value:
        import capo_codepipeline.types.timestamp

        out["startTime"] = capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "last_update_time" in value:
        import capo_codepipeline.types.timestamp

        out["lastUpdateTime"] = (
            capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
                value["last_update_time"]
            )
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "status" in value:
        import capo_codepipeline.types.action_execution_status

        out["status"] = (
            capo_codepipeline.types.action_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "input" in value:
        import capo_codepipeline.types.action_execution_input

        out["input"] = (
            capo_codepipeline.types.action_execution_input.serialize_aws_json_1_1(
                value["input"]
            )
        )
    if "output" in value:
        import capo_codepipeline.types.action_execution_output

        out["output"] = (
            capo_codepipeline.types.action_execution_output.serialize_aws_json_1_1(
                value["output"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionExecutionDetail:
    out: ActionExecutionDetail = {}  # type: ignore[typeddict-item]
    if "pipelineExecutionId" in data:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    if "actionExecutionId" in data:
        out["action_execution_id"] = data["actionExecutionId"]
    if "pipelineVersion" in data:
        out["pipeline_version"] = data["pipelineVersion"]
    if "stageName" in data:
        out["stage_name"] = data["stageName"]
    if "actionName" in data:
        out["action_name"] = data["actionName"]
    if "startTime" in data:
        import capo_codepipeline.types.timestamp

        out["start_time"] = capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["startTime"]
        )
    if "lastUpdateTime" in data:
        import capo_codepipeline.types.timestamp

        out["last_update_time"] = (
            capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
                data["lastUpdateTime"]
            )
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "status" in data:
        import capo_codepipeline.types.action_execution_status

        out["status"] = (
            capo_codepipeline.types.action_execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "input" in data:
        import capo_codepipeline.types.action_execution_input

        out["input"] = (
            capo_codepipeline.types.action_execution_input.deserialize_aws_json_1_1(
                data["input"]
            )
        )
    if "output" in data:
        import capo_codepipeline.types.action_execution_output

        out["output"] = (
            capo_codepipeline.types.action_execution_output.deserialize_aws_json_1_1(
                data["output"]
            )
        )
    return out
