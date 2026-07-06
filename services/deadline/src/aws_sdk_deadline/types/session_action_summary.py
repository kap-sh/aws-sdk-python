"""Generated from Smithy shape ``com.amazonaws.deadline#SessionActionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.ended_at
    import aws_sdk_deadline.types.session_action_definition_summary
    import aws_sdk_deadline.types.session_action_id
    import aws_sdk_deadline.types.session_action_progress_percent
    import aws_sdk_deadline.types.session_action_status
    import aws_sdk_deadline.types.started_at
    import aws_sdk_deadline.types.task_run_manifest_properties_list_response
    import aws_sdk_deadline.types.timestamp


class SessionActionSummary(TypedDict, closed=True):
    session_action_id: "aws_sdk_deadline.types.session_action_id.SessionActionId"
    """<p>The session action ID.</p>"""
    status: "aws_sdk_deadline.types.session_action_status.SessionActionStatus"
    """<p>The status of the session action.</p>"""
    started_at: NotRequired["aws_sdk_deadline.types.started_at.StartedAt"]
    """<p>The date and time the resource started running.</p>"""
    ended_at: NotRequired["aws_sdk_deadline.types.ended_at.EndedAt"]
    """<p>The date and time the resource ended running.</p>"""
    worker_updated_at: NotRequired["aws_sdk_deadline.types.timestamp.Timestamp"]
    """<p>The Linux timestamp of the last date and time that the session action was updated.</p>"""
    progress_percent: NotRequired[
        "aws_sdk_deadline.types.session_action_progress_percent.SessionActionProgressPercent"
    ]
    """<p>The completion percentage for the session action.</p>"""
    manifests: NotRequired[
        "aws_sdk_deadline.types.task_run_manifest_properties_list_response.TaskRunManifestPropertiesListResponse"
    ]
    """<p>The list of manifest properties that describe file attachments for the task run.</p>"""
    definition: "aws_sdk_deadline.types.session_action_definition_summary.SessionActionDefinitionSummary"
    """<p>The session action definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionActionSummary) -> dict:
    out: dict = {}
    out["sessionActionId"] = value["session_action_id"]
    import aws_sdk_deadline.types.session_action_status

    out["status"] = aws_sdk_deadline.types.session_action_status.serialize_json(
        value["status"]
    )
    if "started_at" in value:
        import aws_sdk_deadline.types.started_at

        out["startedAt"] = aws_sdk_deadline.types.started_at.serialize_json(
            value["started_at"]
        )
    if "ended_at" in value:
        import aws_sdk_deadline.types.ended_at

        out["endedAt"] = aws_sdk_deadline.types.ended_at.serialize_json(
            value["ended_at"]
        )
    if "worker_updated_at" in value:
        import aws_sdk_deadline.types.timestamp

        out["workerUpdatedAt"] = aws_sdk_deadline.types.timestamp.serialize_json(
            value["worker_updated_at"]
        )
    if "progress_percent" in value:
        out["progressPercent"] = value["progress_percent"]
    if "manifests" in value:
        import aws_sdk_deadline.types.task_run_manifest_properties_list_response

        out["manifests"] = (
            aws_sdk_deadline.types.task_run_manifest_properties_list_response.serialize_json(
                value["manifests"]
            )
        )
    import aws_sdk_deadline.types.session_action_definition_summary

    out["definition"] = (
        aws_sdk_deadline.types.session_action_definition_summary.serialize_json(
            value["definition"]
        )
    )
    return out


def deserialize_json(data: dict) -> SessionActionSummary:
    out: SessionActionSummary = {}  # type: ignore[typeddict-item]
    if "sessionActionId" in data:
        out["session_action_id"] = data["sessionActionId"]
    else:
        raise DeserializationError("SessionActionSummary.session_action_id required")
    if "status" in data:
        import aws_sdk_deadline.types.session_action_status

        out["status"] = aws_sdk_deadline.types.session_action_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("SessionActionSummary.status required")
    if "startedAt" in data:
        import aws_sdk_deadline.types.started_at

        out["started_at"] = aws_sdk_deadline.types.started_at.deserialize_json(
            data["startedAt"]
        )
    if "endedAt" in data:
        import aws_sdk_deadline.types.ended_at

        out["ended_at"] = aws_sdk_deadline.types.ended_at.deserialize_json(
            data["endedAt"]
        )
    if "workerUpdatedAt" in data:
        import aws_sdk_deadline.types.timestamp

        out["worker_updated_at"] = aws_sdk_deadline.types.timestamp.deserialize_json(
            data["workerUpdatedAt"]
        )
    if "progressPercent" in data:
        out["progress_percent"] = data["progressPercent"]
    if "manifests" in data:
        import aws_sdk_deadline.types.task_run_manifest_properties_list_response

        out["manifests"] = (
            aws_sdk_deadline.types.task_run_manifest_properties_list_response.deserialize_json(
                data["manifests"]
            )
        )
    if "definition" in data:
        import aws_sdk_deadline.types.session_action_definition_summary

        out["definition"] = (
            aws_sdk_deadline.types.session_action_definition_summary.deserialize_json(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("SessionActionSummary.definition required")
    return out
