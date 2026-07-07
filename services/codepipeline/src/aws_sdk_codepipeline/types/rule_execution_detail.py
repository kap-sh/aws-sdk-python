"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleExecutionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.last_updated_by
    import aws_sdk_codepipeline.types.pipeline_execution_id
    import aws_sdk_codepipeline.types.pipeline_version
    import aws_sdk_codepipeline.types.rule_execution_id
    import aws_sdk_codepipeline.types.rule_execution_input
    import aws_sdk_codepipeline.types.rule_execution_output
    import aws_sdk_codepipeline.types.rule_execution_status
    import aws_sdk_codepipeline.types.rule_name
    import aws_sdk_codepipeline.types.stage_name
    import aws_sdk_codepipeline.types.timestamp


class RuleExecutionDetail(TypedDict, closed=True):
    pipeline_execution_id: NotRequired[
        "aws_sdk_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    ]
    """<p>The ID of the pipeline execution in the stage where the rule was run. Use the <a>GetPipelineState</a> action to retrieve the current pipelineExecutionId of the stage.</p>"""
    rule_execution_id: NotRequired[
        "aws_sdk_codepipeline.types.rule_execution_id.RuleExecutionId"
    ]
    """<p>The ID of the run for the rule.</p>"""
    pipeline_version: NotRequired[
        "aws_sdk_codepipeline.types.pipeline_version.PipelineVersion"
    ]
    """<p>The version number of the pipeline with the stage where the rule was run.</p>"""
    stage_name: NotRequired["aws_sdk_codepipeline.types.stage_name.StageName"]
    """<p>The name of the stage where the rule was run.</p>"""
    rule_name: NotRequired["aws_sdk_codepipeline.types.rule_name.RuleName"]
    """<p>The name of the rule that was run in the stage.</p>"""
    start_time: NotRequired["aws_sdk_codepipeline.types.timestamp.Timestamp"]
    """<p>The start time of the rule execution.</p>"""
    last_update_time: NotRequired["aws_sdk_codepipeline.types.timestamp.Timestamp"]
    """<p>The date and time of the last change to the rule execution, in timestamp format.</p>"""
    updated_by: NotRequired["aws_sdk_codepipeline.types.last_updated_by.LastUpdatedBy"]
    """<p>The ARN of the user who changed the rule execution details.</p>"""
    status: NotRequired[
        "aws_sdk_codepipeline.types.rule_execution_status.RuleExecutionStatus"
    ]
    """<p>The status of the rule execution. Status categories are <code>InProgress</code>, <code>Succeeded</code>, and <code>Failed</code>. </p>"""
    input: NotRequired[
        "aws_sdk_codepipeline.types.rule_execution_input.RuleExecutionInput"
    ]
    """<p>Input details for the rule execution, such as role ARN, Region, and input artifacts.</p>"""
    output: NotRequired[
        "aws_sdk_codepipeline.types.rule_execution_output.RuleExecutionOutput"
    ]
    """<p>Output details for the rule execution, such as the rule execution result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleExecutionDetail) -> dict:
    out: dict = {}
    if "pipeline_execution_id" in value:
        out["pipelineExecutionId"] = value["pipeline_execution_id"]
    if "rule_execution_id" in value:
        out["ruleExecutionId"] = value["rule_execution_id"]
    if "pipeline_version" in value:
        out["pipelineVersion"] = value["pipeline_version"]
    if "stage_name" in value:
        out["stageName"] = value["stage_name"]
    if "rule_name" in value:
        out["ruleName"] = value["rule_name"]
    if "start_time" in value:
        import aws_sdk_codepipeline.types.timestamp

        out["startTime"] = aws_sdk_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "last_update_time" in value:
        import aws_sdk_codepipeline.types.timestamp

        out["lastUpdateTime"] = (
            aws_sdk_codepipeline.types.timestamp.serialize_aws_json_1_1(
                value["last_update_time"]
            )
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "status" in value:
        import aws_sdk_codepipeline.types.rule_execution_status

        out["status"] = (
            aws_sdk_codepipeline.types.rule_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "input" in value:
        import aws_sdk_codepipeline.types.rule_execution_input

        out["input"] = (
            aws_sdk_codepipeline.types.rule_execution_input.serialize_aws_json_1_1(
                value["input"]
            )
        )
    if "output" in value:
        import aws_sdk_codepipeline.types.rule_execution_output

        out["output"] = (
            aws_sdk_codepipeline.types.rule_execution_output.serialize_aws_json_1_1(
                value["output"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleExecutionDetail:
    out: RuleExecutionDetail = {}  # type: ignore[typeddict-item]
    if "pipelineExecutionId" in data:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    if "ruleExecutionId" in data:
        out["rule_execution_id"] = data["ruleExecutionId"]
    if "pipelineVersion" in data:
        out["pipeline_version"] = data["pipelineVersion"]
    if "stageName" in data:
        out["stage_name"] = data["stageName"]
    if "ruleName" in data:
        out["rule_name"] = data["ruleName"]
    if "startTime" in data:
        import aws_sdk_codepipeline.types.timestamp

        out["start_time"] = (
            aws_sdk_codepipeline.types.timestamp.deserialize_aws_json_1_1(
                data["startTime"]
            )
        )
    if "lastUpdateTime" in data:
        import aws_sdk_codepipeline.types.timestamp

        out["last_update_time"] = (
            aws_sdk_codepipeline.types.timestamp.deserialize_aws_json_1_1(
                data["lastUpdateTime"]
            )
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "status" in data:
        import aws_sdk_codepipeline.types.rule_execution_status

        out["status"] = (
            aws_sdk_codepipeline.types.rule_execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "input" in data:
        import aws_sdk_codepipeline.types.rule_execution_input

        out["input"] = (
            aws_sdk_codepipeline.types.rule_execution_input.deserialize_aws_json_1_1(
                data["input"]
            )
        )
    if "output" in data:
        import aws_sdk_codepipeline.types.rule_execution_output

        out["output"] = (
            aws_sdk_codepipeline.types.rule_execution_output.deserialize_aws_json_1_1(
                data["output"]
            )
        )
    return out
