"""Generated from Smithy shape ``com.amazonaws.iot#AwsJobExecutionsRolloutConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_job_exponential_rollout_rate
    import aws_sdk_iot.types.maximum_per_minute


class AwsJobExecutionsRolloutConfig(TypedDict):
    maximum_per_minute: NotRequired[
        "aws_sdk_iot.types.maximum_per_minute.MaximumPerMinute"
    ]
    """<p>The maximum number of OTA update job executions started per minute.</p>"""
    exponential_rate: NotRequired[
        "aws_sdk_iot.types.aws_job_exponential_rollout_rate.AwsJobExponentialRolloutRate"
    ]
    """<p>The rate of increase for a job rollout. This parameter allows you to define an exponential rate increase for a job rollout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsJobExecutionsRolloutConfig) -> dict:
    out: dict = {}
    if "maximum_per_minute" in value:
        out["maximumPerMinute"] = value["maximum_per_minute"]
    if "exponential_rate" in value:
        import aws_sdk_iot.types.aws_job_exponential_rollout_rate

        out["exponentialRate"] = (
            aws_sdk_iot.types.aws_job_exponential_rollout_rate.serialize_json(
                value["exponential_rate"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsJobExecutionsRolloutConfig:
    out: AwsJobExecutionsRolloutConfig = {}  # type: ignore[typeddict-item]
    if "maximumPerMinute" in data:
        out["maximum_per_minute"] = data["maximumPerMinute"]
    if "exponentialRate" in data:
        import aws_sdk_iot.types.aws_job_exponential_rollout_rate

        out["exponential_rate"] = (
            aws_sdk_iot.types.aws_job_exponential_rollout_rate.deserialize_json(
                data["exponentialRate"]
            )
        )
    return out
