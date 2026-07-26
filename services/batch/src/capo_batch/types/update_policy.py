"""Generated from Smithy shape ``com.amazonaws.batch#UpdatePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.boolean
    import capo_batch.types.job_execution_timeout_minutes


class UpdatePolicy(TypedDict, closed=True):
    terminate_jobs_on_update: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Specifies whether jobs are automatically terminated when the compute environment infrastructure is updated. The default value is <code>false</code>.</p>"""
    job_execution_timeout_minutes: NotRequired[
        "capo_batch.types.job_execution_timeout_minutes.JobExecutionTimeoutMinutes"
    ]
    """<p>Specifies the job timeout (in minutes) when the compute environment infrastructure is updated. The default value is 30. The maximum value is 7200.</p> <note> <p>Increasing <code>jobExecutionTimeoutMinutes</code> during infrastructure updates delays the replacement of instances with new instances that include updates such as security patches, but provides more time for jobs to execute. Consider the security implications of this tradeoff when setting timeout values.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePolicy) -> dict:
    out: dict = {}
    if "terminate_jobs_on_update" in value:
        out["terminateJobsOnUpdate"] = value["terminate_jobs_on_update"]
    if "job_execution_timeout_minutes" in value:
        out["jobExecutionTimeoutMinutes"] = value["job_execution_timeout_minutes"]
    return out


def deserialize_json(data: dict) -> UpdatePolicy:
    out: UpdatePolicy = {}  # type: ignore[typeddict-item]
    if "terminateJobsOnUpdate" in data:
        out["terminate_jobs_on_update"] = data["terminateJobsOnUpdate"]
    if "jobExecutionTimeoutMinutes" in data:
        out["job_execution_timeout_minutes"] = data["jobExecutionTimeoutMinutes"]
    return out
