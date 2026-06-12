"""Generated from Smithy shape ``com.amazonaws.greengrassv2#IoTJobTimeoutConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.io_t_job_in_progress_timeout_in_minutes


class IoTJobTimeoutConfig(TypedDict):
    in_progress_timeout_in_minutes: NotRequired[
        "aws_sdk_greengrassv2.types.io_t_job_in_progress_timeout_in_minutes.IoTJobInProgressTimeoutInMinutes"
    ]
    """<p>The amount of time, in minutes, that devices have to complete the job. The timer starts when the job status is set to <code>IN_PROGRESS</code>. If the job status doesn't change to a terminal state before the time expires, then the job status is set to <code>TIMED_OUT</code>.</p> <p>The timeout interval must be between 1 minute and 7 days (10080 minutes).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IoTJobTimeoutConfig) -> dict:
    out: dict = {}
    if "in_progress_timeout_in_minutes" in value:
        out["inProgressTimeoutInMinutes"] = value["in_progress_timeout_in_minutes"]
    return out


def deserialize_json(data: dict) -> IoTJobTimeoutConfig:
    out: IoTJobTimeoutConfig = {}  # type: ignore[typeddict-item]
    if "inProgressTimeoutInMinutes" in data:
        out["in_progress_timeout_in_minutes"] = data["inProgressTimeoutInMinutes"]
    return out
