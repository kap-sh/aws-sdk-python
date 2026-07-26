"""Generated from Smithy shape ``com.amazonaws.greengrassv2#IoTJobExponentialRolloutRate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_greengrassv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_greengrassv2.types.io_t_job_rate_increase_criteria
    import capo_greengrassv2.types.io_t_job_rollout_base_rate_per_minute
    import capo_greengrassv2.types.io_t_job_rollout_increment_factor


class IoTJobExponentialRolloutRate(TypedDict, closed=True):
    base_rate_per_minute: "capo_greengrassv2.types.io_t_job_rollout_base_rate_per_minute.IoTJobRolloutBaseRatePerMinute"
    """<p>The minimum number of devices that receive a pending job notification, per minute, when the job starts. This parameter defines the initial rollout rate of the job.</p>"""
    increment_factor: "capo_greengrassv2.types.io_t_job_rollout_increment_factor.IoTJobRolloutIncrementFactor"
    """<p>The exponential factor to increase the rollout rate for the job.</p> <p>This parameter supports up to one digit after the decimal (for example, you can specify <code>1.5</code>, but not <code>1.55</code>).</p>"""
    rate_increase_criteria: "capo_greengrassv2.types.io_t_job_rate_increase_criteria.IoTJobRateIncreaseCriteria"
    """<p>The criteria to increase the rollout rate for the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IoTJobExponentialRolloutRate) -> dict:
    out: dict = {}
    out["baseRatePerMinute"] = value["base_rate_per_minute"]
    out["incrementFactor"] = value["increment_factor"]
    import capo_greengrassv2.types.io_t_job_rate_increase_criteria

    out["rateIncreaseCriteria"] = (
        capo_greengrassv2.types.io_t_job_rate_increase_criteria.serialize_json(
            value["rate_increase_criteria"]
        )
    )
    return out


def deserialize_json(data: dict) -> IoTJobExponentialRolloutRate:
    out: IoTJobExponentialRolloutRate = {}  # type: ignore[typeddict-item]
    if "baseRatePerMinute" in data:
        out["base_rate_per_minute"] = data["baseRatePerMinute"]
    else:
        raise DeserializationError(
            "IoTJobExponentialRolloutRate.base_rate_per_minute required"
        )
    if "incrementFactor" in data:
        out["increment_factor"] = data["incrementFactor"]
    else:
        raise DeserializationError(
            "IoTJobExponentialRolloutRate.increment_factor required"
        )
    if "rateIncreaseCriteria" in data:
        import capo_greengrassv2.types.io_t_job_rate_increase_criteria

        out["rate_increase_criteria"] = (
            capo_greengrassv2.types.io_t_job_rate_increase_criteria.deserialize_json(
                data["rateIncreaseCriteria"]
            )
        )
    else:
        raise DeserializationError(
            "IoTJobExponentialRolloutRate.rate_increase_criteria required"
        )
    return out
