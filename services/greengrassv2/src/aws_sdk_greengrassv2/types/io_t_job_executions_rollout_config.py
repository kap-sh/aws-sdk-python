"""Generated from Smithy shape ``com.amazonaws.greengrassv2#IoTJobExecutionsRolloutConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.io_t_job_exponential_rollout_rate
    import aws_sdk_greengrassv2.types.io_t_job_max_executions_per_min


class IoTJobExecutionsRolloutConfig(TypedDict, closed=True):
    exponential_rate: NotRequired[
        "aws_sdk_greengrassv2.types.io_t_job_exponential_rollout_rate.IoTJobExponentialRolloutRate"
    ]
    """<p>The exponential rate to increase the job rollout rate.</p>"""
    maximum_per_minute: NotRequired[
        "aws_sdk_greengrassv2.types.io_t_job_max_executions_per_min.IoTJobMaxExecutionsPerMin"
    ]
    """<p>The maximum number of devices that receive a pending job notification, per minute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IoTJobExecutionsRolloutConfig) -> dict:
    out: dict = {}
    if "exponential_rate" in value:
        import aws_sdk_greengrassv2.types.io_t_job_exponential_rollout_rate

        out["exponentialRate"] = (
            aws_sdk_greengrassv2.types.io_t_job_exponential_rollout_rate.serialize_json(
                value["exponential_rate"]
            )
        )
    if "maximum_per_minute" in value:
        out["maximumPerMinute"] = value["maximum_per_minute"]
    return out


def deserialize_json(data: dict) -> IoTJobExecutionsRolloutConfig:
    out: IoTJobExecutionsRolloutConfig = {}  # type: ignore[typeddict-item]
    if "exponentialRate" in data:
        import aws_sdk_greengrassv2.types.io_t_job_exponential_rollout_rate

        out["exponential_rate"] = (
            aws_sdk_greengrassv2.types.io_t_job_exponential_rollout_rate.deserialize_json(
                data["exponentialRate"]
            )
        )
    if "maximumPerMinute" in data:
        out["maximum_per_minute"] = data["maximumPerMinute"]
    return out
