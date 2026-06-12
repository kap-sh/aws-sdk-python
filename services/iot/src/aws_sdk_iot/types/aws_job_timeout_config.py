"""Generated from Smithy shape ``com.amazonaws.iot#AwsJobTimeoutConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_job_timeout_in_progress_timeout_in_minutes


class AwsJobTimeoutConfig(TypedDict):
    in_progress_timeout_in_minutes: NotRequired[
        "aws_sdk_iot.types.aws_job_timeout_in_progress_timeout_in_minutes.AwsJobTimeoutInProgressTimeoutInMinutes"
    ]
    """<p>Specifies the amount of time, in minutes, this device has to finish execution of this job. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in progress timer can't be updated and will apply to all job executions for the job. Whenever a job execution remains in the IN_PROGRESS status for longer than this interval, the job execution will fail and switch to the terminal <code>TIMED_OUT</code> status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsJobTimeoutConfig) -> dict:
    out: dict = {}
    if "in_progress_timeout_in_minutes" in value:
        out["inProgressTimeoutInMinutes"] = value["in_progress_timeout_in_minutes"]
    return out


def deserialize_json(data: dict) -> AwsJobTimeoutConfig:
    out: AwsJobTimeoutConfig = {}  # type: ignore[typeddict-item]
    if "inProgressTimeoutInMinutes" in data:
        out["in_progress_timeout_in_minutes"] = data["inProgressTimeoutInMinutes"]
    return out
