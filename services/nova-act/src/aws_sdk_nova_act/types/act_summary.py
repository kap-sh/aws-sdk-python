"""Generated from Smithy shape ``com.amazonaws.novaact#ActSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.act_status
    import aws_sdk_nova_act.types.date_timestamp
    import aws_sdk_nova_act.types.trace_location
    import aws_sdk_nova_act.types.uuid_string


class ActSummary(TypedDict):
    workflow_run_id: "aws_sdk_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the workflow run containing this act.</p>"""
    session_id: "aws_sdk_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the session containing this act.</p>"""
    act_id: "aws_sdk_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the act.</p>"""
    status: "aws_sdk_nova_act.types.act_status.ActStatus"
    """<p>The current execution status of the act.</p>"""
    started_at: "aws_sdk_nova_act.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the act started execution.</p>"""
    ended_at: NotRequired["aws_sdk_nova_act.types.date_timestamp.DateTimestamp"]
    """<p>The timestamp when the act completed execution, if applicable.</p>"""
    trace_location: NotRequired["aws_sdk_nova_act.types.trace_location.TraceLocation"]
    """<p>The location where trace information for this act is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActSummary) -> dict:
    out: dict = {}
    out["workflowRunId"] = value["workflow_run_id"]
    out["sessionId"] = value["session_id"]
    out["actId"] = value["act_id"]
    import aws_sdk_nova_act.types.act_status

    out["status"] = aws_sdk_nova_act.types.act_status.serialize_json(value["status"])
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


def deserialize_json(data: dict) -> ActSummary:
    out: ActSummary = {}  # type: ignore[typeddict-item]
    if "workflowRunId" in data:
        out["workflow_run_id"] = data["workflowRunId"]
    else:
        raise DeserializationError("ActSummary.workflow_run_id required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("ActSummary.session_id required")
    if "actId" in data:
        out["act_id"] = data["actId"]
    else:
        raise DeserializationError("ActSummary.act_id required")
    if "status" in data:
        import aws_sdk_nova_act.types.act_status

        out["status"] = aws_sdk_nova_act.types.act_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("ActSummary.status required")
    if "startedAt" in data:
        import aws_sdk_nova_act.types.date_timestamp

        out["started_at"] = aws_sdk_nova_act.types.date_timestamp.deserialize_json(
            data["startedAt"]
        )
    else:
        raise DeserializationError("ActSummary.started_at required")
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
