"""Generated from Smithy shape ``com.amazonaws.glue#WorkflowRunStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.integer_value


class WorkflowRunStatistics(TypedDict, closed=True):
    total_actions: "aws_sdk_glue.types.integer_value.IntegerValue"
    """<p>Total number of Actions in the workflow run.</p>"""
    timeout_actions: "aws_sdk_glue.types.integer_value.IntegerValue"
    """<p>Total number of Actions that timed out.</p>"""
    failed_actions: "aws_sdk_glue.types.integer_value.IntegerValue"
    """<p>Total number of Actions that have failed.</p>"""
    stopped_actions: "aws_sdk_glue.types.integer_value.IntegerValue"
    """<p>Total number of Actions that have stopped.</p>"""
    succeeded_actions: "aws_sdk_glue.types.integer_value.IntegerValue"
    """<p>Total number of Actions that have succeeded.</p>"""
    running_actions: "aws_sdk_glue.types.integer_value.IntegerValue"
    """<p>Total number Actions in running state.</p>"""
    errored_actions: "aws_sdk_glue.types.integer_value.IntegerValue"
    """<p>Indicates the count of job runs in the ERROR state in the workflow run.</p>"""
    waiting_actions: "aws_sdk_glue.types.integer_value.IntegerValue"
    """<p>Indicates the count of job runs in WAITING state in the workflow run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkflowRunStatistics) -> dict:
    out: dict = {}
    out["TotalActions"] = value.get("total_actions", 0)
    out["TimeoutActions"] = value.get("timeout_actions", 0)
    out["FailedActions"] = value.get("failed_actions", 0)
    out["StoppedActions"] = value.get("stopped_actions", 0)
    out["SucceededActions"] = value.get("succeeded_actions", 0)
    out["RunningActions"] = value.get("running_actions", 0)
    out["ErroredActions"] = value.get("errored_actions", 0)
    out["WaitingActions"] = value.get("waiting_actions", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkflowRunStatistics:
    out: WorkflowRunStatistics = {}  # type: ignore[typeddict-item]
    if "TotalActions" in data:
        out["total_actions"] = data["TotalActions"]
    else:
        out["total_actions"] = 0
    if "TimeoutActions" in data:
        out["timeout_actions"] = data["TimeoutActions"]
    else:
        out["timeout_actions"] = 0
    if "FailedActions" in data:
        out["failed_actions"] = data["FailedActions"]
    else:
        out["failed_actions"] = 0
    if "StoppedActions" in data:
        out["stopped_actions"] = data["StoppedActions"]
    else:
        out["stopped_actions"] = 0
    if "SucceededActions" in data:
        out["succeeded_actions"] = data["SucceededActions"]
    else:
        out["succeeded_actions"] = 0
    if "RunningActions" in data:
        out["running_actions"] = data["RunningActions"]
    else:
        out["running_actions"] = 0
    if "ErroredActions" in data:
        out["errored_actions"] = data["ErroredActions"]
    else:
        out["errored_actions"] = 0
    if "WaitingActions" in data:
        out["waiting_actions"] = data["WaitingActions"]
    else:
        out["waiting_actions"] = 0
    return out
