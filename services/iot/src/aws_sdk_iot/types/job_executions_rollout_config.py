"""Generated from Smithy shape ``com.amazonaws.iot#JobExecutionsRolloutConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.exponential_rollout_rate
    import aws_sdk_iot.types.max_job_executions_per_min


class JobExecutionsRolloutConfig(TypedDict, closed=True):
    maximum_per_minute: NotRequired[
        "aws_sdk_iot.types.max_job_executions_per_min.MaxJobExecutionsPerMin"
    ]
    """<p>The maximum number of things that will be notified of a pending job, per minute. This parameter allows you to create a staged rollout.</p>"""
    exponential_rate: NotRequired[
        "aws_sdk_iot.types.exponential_rollout_rate.ExponentialRolloutRate"
    ]
    """<p>The rate of increase for a job rollout. This parameter allows you to define an exponential rate for a job rollout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobExecutionsRolloutConfig) -> dict:
    out: dict = {}
    if "maximum_per_minute" in value:
        out["maximumPerMinute"] = value["maximum_per_minute"]
    if "exponential_rate" in value:
        import aws_sdk_iot.types.exponential_rollout_rate

        out["exponentialRate"] = (
            aws_sdk_iot.types.exponential_rollout_rate.serialize_json(
                value["exponential_rate"]
            )
        )
    return out


def deserialize_json(data: dict) -> JobExecutionsRolloutConfig:
    out: JobExecutionsRolloutConfig = {}  # type: ignore[typeddict-item]
    if "maximumPerMinute" in data:
        out["maximum_per_minute"] = data["maximumPerMinute"]
    if "exponentialRate" in data:
        import aws_sdk_iot.types.exponential_rollout_rate

        out["exponential_rate"] = (
            aws_sdk_iot.types.exponential_rollout_rate.deserialize_json(
                data["exponentialRate"]
            )
        )
    return out
