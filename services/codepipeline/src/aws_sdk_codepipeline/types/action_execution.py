"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_execution_id
    import aws_sdk_codepipeline.types.action_execution_status
    import aws_sdk_codepipeline.types.action_execution_token
    import aws_sdk_codepipeline.types.error_details
    import aws_sdk_codepipeline.types.execution_id
    import aws_sdk_codepipeline.types.execution_summary
    import aws_sdk_codepipeline.types.last_updated_by
    import aws_sdk_codepipeline.types.log_stream_arn
    import aws_sdk_codepipeline.types.percentage
    import aws_sdk_codepipeline.types.timestamp
    import aws_sdk_codepipeline.types.url


class ActionExecution(TypedDict, closed=True):
    action_execution_id: NotRequired[
        "aws_sdk_codepipeline.types.action_execution_id.ActionExecutionId"
    ]
    """<p>ID of the workflow action execution in the current stage. Use the <a>GetPipelineState</a> action to retrieve the current action execution details of the current stage.</p> <note> <p>For older executions, this field might be empty. The action execution ID is available for executions run on or after March 2020.</p> </note>"""
    status: NotRequired[
        "aws_sdk_codepipeline.types.action_execution_status.ActionExecutionStatus"
    ]
    """<p>The status of the action, or for a completed action, the last status of the action.</p>"""
    summary: NotRequired[
        "aws_sdk_codepipeline.types.execution_summary.ExecutionSummary"
    ]
    """<p>A summary of the run of the action.</p>"""
    last_status_change: NotRequired["aws_sdk_codepipeline.types.timestamp.Timestamp"]
    """<p>The last status change of the action.</p>"""
    token: NotRequired[
        "aws_sdk_codepipeline.types.action_execution_token.ActionExecutionToken"
    ]
    """<p>The system-generated token used to identify a unique approval request. The token for each open approval request can be obtained using the <code>GetPipelineState</code> command. It is used to validate that the approval request corresponding to this token is still valid.</p>"""
    last_updated_by: NotRequired[
        "aws_sdk_codepipeline.types.last_updated_by.LastUpdatedBy"
    ]
    """<p>The ARN of the user who last changed the pipeline.</p>"""
    external_execution_id: NotRequired[
        "aws_sdk_codepipeline.types.execution_id.ExecutionId"
    ]
    """<p>The external ID of the run of the action.</p>"""
    external_execution_url: NotRequired["aws_sdk_codepipeline.types.url.Url"]
    """<p>The URL of a resource external to Amazon Web Services that is used when running the action (for example, an external repository URL).</p>"""
    percent_complete: NotRequired["aws_sdk_codepipeline.types.percentage.Percentage"]
    """<p>A percentage of completeness of the action as it runs.</p>"""
    error_details: NotRequired["aws_sdk_codepipeline.types.error_details.ErrorDetails"]
    """<p>The details of an error returned by a URL external to Amazon Web Services.</p>"""
    log_stream_arn: NotRequired[
        "aws_sdk_codepipeline.types.log_stream_arn.LogStreamARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the log stream for the action compute.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionExecution) -> dict:
    out: dict = {}
    if "action_execution_id" in value:
        out["actionExecutionId"] = value["action_execution_id"]
    if "status" in value:
        import aws_sdk_codepipeline.types.action_execution_status

        out["status"] = (
            aws_sdk_codepipeline.types.action_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "summary" in value:
        out["summary"] = value["summary"]
    if "last_status_change" in value:
        import aws_sdk_codepipeline.types.timestamp

        out["lastStatusChange"] = (
            aws_sdk_codepipeline.types.timestamp.serialize_aws_json_1_1(
                value["last_status_change"]
            )
        )
    if "token" in value:
        out["token"] = value["token"]
    if "last_updated_by" in value:
        out["lastUpdatedBy"] = value["last_updated_by"]
    if "external_execution_id" in value:
        out["externalExecutionId"] = value["external_execution_id"]
    if "external_execution_url" in value:
        out["externalExecutionUrl"] = value["external_execution_url"]
    if "percent_complete" in value:
        out["percentComplete"] = value["percent_complete"]
    if "error_details" in value:
        import aws_sdk_codepipeline.types.error_details

        out["errorDetails"] = (
            aws_sdk_codepipeline.types.error_details.serialize_aws_json_1_1(
                value["error_details"]
            )
        )
    if "log_stream_arn" in value:
        out["logStreamARN"] = value["log_stream_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionExecution:
    out: ActionExecution = {}  # type: ignore[typeddict-item]
    if "actionExecutionId" in data:
        out["action_execution_id"] = data["actionExecutionId"]
    if "status" in data:
        import aws_sdk_codepipeline.types.action_execution_status

        out["status"] = (
            aws_sdk_codepipeline.types.action_execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "summary" in data:
        out["summary"] = data["summary"]
    if "lastStatusChange" in data:
        import aws_sdk_codepipeline.types.timestamp

        out["last_status_change"] = (
            aws_sdk_codepipeline.types.timestamp.deserialize_aws_json_1_1(
                data["lastStatusChange"]
            )
        )
    if "token" in data:
        out["token"] = data["token"]
    if "lastUpdatedBy" in data:
        out["last_updated_by"] = data["lastUpdatedBy"]
    if "externalExecutionId" in data:
        out["external_execution_id"] = data["externalExecutionId"]
    if "externalExecutionUrl" in data:
        out["external_execution_url"] = data["externalExecutionUrl"]
    if "percentComplete" in data:
        out["percent_complete"] = data["percentComplete"]
    if "errorDetails" in data:
        import aws_sdk_codepipeline.types.error_details

        out["error_details"] = (
            aws_sdk_codepipeline.types.error_details.deserialize_aws_json_1_1(
                data["errorDetails"]
            )
        )
    if "logStreamARN" in data:
        out["log_stream_arn"] = data["logStreamARN"]
    return out
