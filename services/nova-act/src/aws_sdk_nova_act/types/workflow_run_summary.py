"""Generated from Smithy shape ``com.amazonaws.novaact#WorkflowRunSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.date_timestamp
    import aws_sdk_nova_act.types.trace_location
    import aws_sdk_nova_act.types.uuid_string
    import aws_sdk_nova_act.types.workflow_run_arn
    import aws_sdk_nova_act.types.workflow_run_status


class WorkflowRunSummary(TypedDict):
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
    trace_location: NotRequired["aws_sdk_nova_act.types.trace_location.TraceLocation"]
    """<p>The location where trace information for this workflow run is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowRunSummary) -> dict:
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
    if "trace_location" in value:
        import aws_sdk_nova_act.types.trace_location

        out["traceLocation"] = aws_sdk_nova_act.types.trace_location.serialize_json(
            value["trace_location"]
        )
    return out


def deserialize_json(data: dict) -> WorkflowRunSummary:
    out: WorkflowRunSummary = {}  # type: ignore[typeddict-item]
    if "workflowRunArn" in data:
        out["workflow_run_arn"] = data["workflowRunArn"]
    else:
        raise DeserializationError("WorkflowRunSummary.workflow_run_arn required")
    if "workflowRunId" in data:
        out["workflow_run_id"] = data["workflowRunId"]
    else:
        raise DeserializationError("WorkflowRunSummary.workflow_run_id required")
    if "status" in data:
        import aws_sdk_nova_act.types.workflow_run_status

        out["status"] = aws_sdk_nova_act.types.workflow_run_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("WorkflowRunSummary.status required")
    if "startedAt" in data:
        import aws_sdk_nova_act.types.date_timestamp

        out["started_at"] = aws_sdk_nova_act.types.date_timestamp.deserialize_json(
            data["startedAt"]
        )
    else:
        raise DeserializationError("WorkflowRunSummary.started_at required")
    if "endedAt" in data:
        import aws_sdk_nova_act.types.date_timestamp

        out["ended_at"] = aws_sdk_nova_act.types.date_timestamp.deserialize_json(
            data["endedAt"]
        )
    if "traceLocation" in data:
        import aws_sdk_nova_act.types.trace_location

        out["trace_location"] = aws_sdk_nova_act.types.trace_location.deserialize_json(
            data["traceLocation"]
        )
    return out
