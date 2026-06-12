"""Generated from Smithy shape ``com.amazonaws.drs#LaunchActionRun``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_drs.types.failure_reason
    import aws_sdk_drs.types.launch_action
    import aws_sdk_drs.types.launch_action_run_id
    import aws_sdk_drs.types.launch_action_run_status

class LaunchActionRun(TypedDict):
    action: NotRequired["aws_sdk_drs.types.launch_action.LaunchAction"]
    """<p>Action.</p>"""
    run_id: NotRequired["aws_sdk_drs.types.launch_action_run_id.LaunchActionRunId"]
    """<p>Run Id.</p>"""
    status: NotRequired["aws_sdk_drs.types.launch_action_run_status.LaunchActionRunStatus"]
    """<p>Run status.</p>"""
    failure_reason: NotRequired["aws_sdk_drs.types.failure_reason.FailureReason"]
    """<p>Failure reason.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: LaunchActionRun) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_drs.types.launch_action
        out["action"] = aws_sdk_drs.types.launch_action.serialize_json(value["action"])
    if "run_id" in value:
        out["runId"] = value["run_id"]
    if "status" in value:
        out["status"] = value["status"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> LaunchActionRun:
    out: LaunchActionRun = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import aws_sdk_drs.types.launch_action
        out["action"] = aws_sdk_drs.types.launch_action.deserialize_json(data["action"])
    if "runId" in data:
        out["run_id"] = data["runId"]
    if "status" in data:
        out["status"] = data["status"]
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out