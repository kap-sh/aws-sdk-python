"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DeploymentIoTJobConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.io_t_job_abort_config
    import capo_greengrassv2.types.io_t_job_executions_rollout_config
    import capo_greengrassv2.types.io_t_job_timeout_config


class DeploymentIoTJobConfiguration(TypedDict, closed=True):
    job_executions_rollout_config: NotRequired[
        "capo_greengrassv2.types.io_t_job_executions_rollout_config.IoTJobExecutionsRolloutConfig"
    ]
    """<p>The rollout configuration for the job. This configuration defines the rate at which the job rolls out to the fleet of target devices.</p>"""
    abort_config: NotRequired[
        "capo_greengrassv2.types.io_t_job_abort_config.IoTJobAbortConfig"
    ]
    """<p>The stop configuration for the job. This configuration defines when and how to stop a job rollout.</p>"""
    timeout_config: NotRequired[
        "capo_greengrassv2.types.io_t_job_timeout_config.IoTJobTimeoutConfig"
    ]
    """<p>The timeout configuration for the job. This configuration defines the amount of time each device has to complete the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentIoTJobConfiguration) -> dict:
    out: dict = {}
    if "job_executions_rollout_config" in value:
        import capo_greengrassv2.types.io_t_job_executions_rollout_config

        out["jobExecutionsRolloutConfig"] = (
            capo_greengrassv2.types.io_t_job_executions_rollout_config.serialize_json(
                value["job_executions_rollout_config"]
            )
        )
    if "abort_config" in value:
        import capo_greengrassv2.types.io_t_job_abort_config

        out["abortConfig"] = (
            capo_greengrassv2.types.io_t_job_abort_config.serialize_json(
                value["abort_config"]
            )
        )
    if "timeout_config" in value:
        import capo_greengrassv2.types.io_t_job_timeout_config

        out["timeoutConfig"] = (
            capo_greengrassv2.types.io_t_job_timeout_config.serialize_json(
                value["timeout_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeploymentIoTJobConfiguration:
    out: DeploymentIoTJobConfiguration = {}  # type: ignore[typeddict-item]
    if "jobExecutionsRolloutConfig" in data:
        import capo_greengrassv2.types.io_t_job_executions_rollout_config

        out["job_executions_rollout_config"] = (
            capo_greengrassv2.types.io_t_job_executions_rollout_config.deserialize_json(
                data["jobExecutionsRolloutConfig"]
            )
        )
    if "abortConfig" in data:
        import capo_greengrassv2.types.io_t_job_abort_config

        out["abort_config"] = (
            capo_greengrassv2.types.io_t_job_abort_config.deserialize_json(
                data["abortConfig"]
            )
        )
    if "timeoutConfig" in data:
        import capo_greengrassv2.types.io_t_job_timeout_config

        out["timeout_config"] = (
            capo_greengrassv2.types.io_t_job_timeout_config.deserialize_json(
                data["timeoutConfig"]
            )
        )
    return out
