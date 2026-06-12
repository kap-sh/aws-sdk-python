"""Generated from Smithy shape ``com.amazonaws.deadline#UpdatedSessionActionInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.completed_status
    import aws_sdk_deadline.types.process_exit_code
    import aws_sdk_deadline.types.session_action_progress_message
    import aws_sdk_deadline.types.session_action_progress_percent
    import aws_sdk_deadline.types.task_run_manifest_properties_list_request
    import aws_sdk_deadline.types.timestamp


class UpdatedSessionActionInfo(TypedDict):
    completed_status: NotRequired[
        "aws_sdk_deadline.types.completed_status.CompletedStatus"
    ]
    """<p>The status of the session upon completion.</p>"""
    process_exit_code: NotRequired[
        "aws_sdk_deadline.types.process_exit_code.ProcessExitCode"
    ]
    """<p>The process exit code. The default Deadline Cloud worker agent converts unsigned 32-bit exit codes to signed 32-bit exit codes.</p>"""
    progress_message: NotRequired[
        "aws_sdk_deadline.types.session_action_progress_message.SessionActionProgressMessage"
    ]
    """<p>A message to indicate the progress of the updated session action.</p>"""
    started_at: NotRequired["aws_sdk_deadline.types.timestamp.Timestamp"]
    """<p>The date and time the resource started running.</p>"""
    ended_at: NotRequired["aws_sdk_deadline.types.timestamp.Timestamp"]
    """<p>The date and time the resource ended running.</p>"""
    updated_at: NotRequired["aws_sdk_deadline.types.timestamp.Timestamp"]
    """<p>The updated time.</p>"""
    progress_percent: NotRequired[
        "aws_sdk_deadline.types.session_action_progress_percent.SessionActionProgressPercent"
    ]
    """<p>The percentage completed.</p>"""
    manifests: NotRequired[
        "aws_sdk_deadline.types.task_run_manifest_properties_list_request.TaskRunManifestPropertiesListRequest"
    ]
    """<p>A list of output manifest properties reported by the worker agent, with each entry corresponding to a manifest property in the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedSessionActionInfo) -> dict:
    out: dict = {}
    if "completed_status" in value:
        import aws_sdk_deadline.types.completed_status

        out["completedStatus"] = aws_sdk_deadline.types.completed_status.serialize_json(
            value["completed_status"]
        )
    if "process_exit_code" in value:
        out["processExitCode"] = value["process_exit_code"]
    if "progress_message" in value:
        out["progressMessage"] = value["progress_message"]
    if "started_at" in value:
        import aws_sdk_deadline.types.timestamp

        out["startedAt"] = aws_sdk_deadline.types.timestamp.serialize_json(
            value["started_at"]
        )
    if "ended_at" in value:
        import aws_sdk_deadline.types.timestamp

        out["endedAt"] = aws_sdk_deadline.types.timestamp.serialize_json(
            value["ended_at"]
        )
    if "updated_at" in value:
        import aws_sdk_deadline.types.timestamp

        out["updatedAt"] = aws_sdk_deadline.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "progress_percent" in value:
        out["progressPercent"] = value["progress_percent"]
    if "manifests" in value:
        import aws_sdk_deadline.types.task_run_manifest_properties_list_request

        out["manifests"] = (
            aws_sdk_deadline.types.task_run_manifest_properties_list_request.serialize_json(
                value["manifests"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedSessionActionInfo:
    out: UpdatedSessionActionInfo = {}  # type: ignore[typeddict-item]
    if "completedStatus" in data:
        import aws_sdk_deadline.types.completed_status

        out["completed_status"] = (
            aws_sdk_deadline.types.completed_status.deserialize_json(
                data["completedStatus"]
            )
        )
    if "processExitCode" in data:
        out["process_exit_code"] = data["processExitCode"]
    if "progressMessage" in data:
        out["progress_message"] = data["progressMessage"]
    if "startedAt" in data:
        import aws_sdk_deadline.types.timestamp

        out["started_at"] = aws_sdk_deadline.types.timestamp.deserialize_json(
            data["startedAt"]
        )
    if "endedAt" in data:
        import aws_sdk_deadline.types.timestamp

        out["ended_at"] = aws_sdk_deadline.types.timestamp.deserialize_json(
            data["endedAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_deadline.types.timestamp

        out["updated_at"] = aws_sdk_deadline.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "progressPercent" in data:
        out["progress_percent"] = data["progressPercent"]
    if "manifests" in data:
        import aws_sdk_deadline.types.task_run_manifest_properties_list_request

        out["manifests"] = (
            aws_sdk_deadline.types.task_run_manifest_properties_list_request.deserialize_json(
                data["manifests"]
            )
        )
    return out
