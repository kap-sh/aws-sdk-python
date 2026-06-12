"""Generated from Smithy shape ``com.amazonaws.batch#JobStateTimeLimitAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.job_state_time_limit_actions_action
    import aws_sdk_batch.types.job_state_time_limit_actions_state
    import aws_sdk_batch.types.string


class JobStateTimeLimitAction(TypedDict):
    reason: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The reason to log for the action being taken.</p>"""
    state: NotRequired[
        "aws_sdk_batch.types.job_state_time_limit_actions_state.JobStateTimeLimitActionsState"
    ]
    """<p>The state of the job needed to trigger the action. The only supported value is <code>RUNNABLE</code>.</p>"""
    max_time_seconds: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The approximate amount of time, in seconds, that must pass with the job in the specified state before the action is taken. The minimum value is 600 (10 minutes) and the maximum value is 86,400 (24 hours).</p>"""
    action: NotRequired[
        "aws_sdk_batch.types.job_state_time_limit_actions_action.JobStateTimeLimitActionsAction"
    ]
    """<p>The action to take when a job is at the head of the job queue in the specified state for the specified period of time. For job queues connected to a <code>ECS</code>, <code>FARGATE</code> or <code>EKS</code> compute environment, the only supported value is <code>CANCEL</code>, which will cancel the job. For job queues connected to a <code>SAGEMAKER_TRAINING</code> service environment, the only supported value is <code>TERMINATE</code>, which will terminate the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobStateTimeLimitAction) -> dict:
    out: dict = {}
    if "reason" in value:
        out["reason"] = value["reason"]
    if "state" in value:
        import aws_sdk_batch.types.job_state_time_limit_actions_state

        out["state"] = (
            aws_sdk_batch.types.job_state_time_limit_actions_state.serialize_json(
                value["state"]
            )
        )
    if "max_time_seconds" in value:
        out["maxTimeSeconds"] = value["max_time_seconds"]
    if "action" in value:
        import aws_sdk_batch.types.job_state_time_limit_actions_action

        out["action"] = (
            aws_sdk_batch.types.job_state_time_limit_actions_action.serialize_json(
                value["action"]
            )
        )
    return out


def deserialize_json(data: dict) -> JobStateTimeLimitAction:
    out: JobStateTimeLimitAction = {}  # type: ignore[typeddict-item]
    if "reason" in data:
        out["reason"] = data["reason"]
    if "state" in data:
        import aws_sdk_batch.types.job_state_time_limit_actions_state

        out["state"] = (
            aws_sdk_batch.types.job_state_time_limit_actions_state.deserialize_json(
                data["state"]
            )
        )
    if "maxTimeSeconds" in data:
        out["max_time_seconds"] = data["maxTimeSeconds"]
    if "action" in data:
        import aws_sdk_batch.types.job_state_time_limit_actions_action

        out["action"] = (
            aws_sdk_batch.types.job_state_time_limit_actions_action.deserialize_json(
                data["action"]
            )
        )
    return out
