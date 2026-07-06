"""Generated from Smithy shape ``com.amazonaws.novaact#GetWorkflowRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.cloud_watch_log_group_name
    import aws_sdk_nova_act.types.date_timestamp
    import aws_sdk_nova_act.types.model_id
    import aws_sdk_nova_act.types.uuid_string
    import aws_sdk_nova_act.types.workflow_run_arn
    import aws_sdk_nova_act.types.workflow_run_status


class GetWorkflowRunResponse(TypedDict, closed=True):
    workflow_run_arn: "aws_sdk_nova_act.types.workflow_run_arn.WorkflowRunArn"
    """<p>The Amazon Resource Name (ARN) of the workflow run.</p>"""
    workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the workflow run.</p>"""
    status: "aws_sdk_nova_act.types.workflow_run_status.WorkflowRunStatus"
    """<p>The current execution status of the workflow run.</p>"""
    started_at: "aws_sdk_nova_act.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the workflow run started execution.</p>"""
    ended_at: NotRequired["aws_sdk_nova_act.types.date_timestamp.DateTimestamp"]
    """<p>The timestamp when the workflow run completed execution, if applicable.</p>"""
    model_id: "aws_sdk_nova_act.types.model_id.ModelId"
    """<p>The ID of the AI model being used for this workflow run.</p>"""
    log_group_name: NotRequired[
        "aws_sdk_nova_act.types.cloud_watch_log_group_name.CloudWatchLogGroupName"
    ]
    """<p>The CloudWatch log group name for this workflow run's logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowRunResponse) -> dict:
    out: dict = {}
    out["workflowRunArn"] = value["workflow_run_arn"]
    out["workflowRunId"] = value["workflow_run_id"]
    import aws_sdk_nova_act.types.workflow_run_status

    out["status"] = aws_sdk_nova_act.types.workflow_run_status.serialize_json(
        value["status"]
    )
    import aws_sdk_nova_act.types.date_timestamp

    out["startedAt"] = aws_sdk_nova_act.types.date_timestamp.serialize_json(
        value["started_at"]
    )
    if "ended_at" in value:
        import aws_sdk_nova_act.types.date_timestamp

        out["endedAt"] = aws_sdk_nova_act.types.date_timestamp.serialize_json(
            value["ended_at"]
        )
    out["modelId"] = value["model_id"]
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    return out


def deserialize_json(data: dict) -> GetWorkflowRunResponse:
    out: GetWorkflowRunResponse = {}  # type: ignore[typeddict-item]
    if "workflowRunArn" in data:
        out["workflow_run_arn"] = data["workflowRunArn"]
    else:
        raise DeserializationError("GetWorkflowRunResponse.workflow_run_arn required")
    if "workflowRunId" in data:
        out["workflow_run_id"] = data["workflowRunId"]
    else:
        raise DeserializationError("GetWorkflowRunResponse.workflow_run_id required")
    if "status" in data:
        import aws_sdk_nova_act.types.workflow_run_status

        out["status"] = aws_sdk_nova_act.types.workflow_run_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetWorkflowRunResponse.status required")
    if "startedAt" in data:
        import aws_sdk_nova_act.types.date_timestamp

        out["started_at"] = aws_sdk_nova_act.types.date_timestamp.deserialize_json(
            data["startedAt"]
        )
    else:
        raise DeserializationError("GetWorkflowRunResponse.started_at required")
    if "endedAt" in data:
        import aws_sdk_nova_act.types.date_timestamp

        out["ended_at"] = aws_sdk_nova_act.types.date_timestamp.deserialize_json(
            data["endedAt"]
        )
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("GetWorkflowRunResponse.model_id required")
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    return out
