"""Generated from Smithy shape ``com.amazonaws.iot#ExponentialRolloutRate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.increment_factor
    import capo_iot.types.rate_increase_criteria
    import capo_iot.types.rollout_rate_per_minute


class ExponentialRolloutRate(TypedDict, closed=True):
    base_rate_per_minute: "capo_iot.types.rollout_rate_per_minute.RolloutRatePerMinute"
    """<p>The minimum number of things that will be notified of a pending job, per minute at the start of job rollout. This parameter allows you to define the initial rate of rollout.</p>"""
    increment_factor: "capo_iot.types.increment_factor.IncrementFactor"
    """<p>The exponential factor to increase the rate of rollout for a job.</p> <p>Amazon Web Services IoT Core supports up to one digit after the decimal (for example, 1.5, but not 1.55).</p>"""
    rate_increase_criteria: "capo_iot.types.rate_increase_criteria.RateIncreaseCriteria"
    """<p>The criteria to initiate the increase in rate of rollout for a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExponentialRolloutRate) -> dict:
    out: dict = {}
    out["baseRatePerMinute"] = value["base_rate_per_minute"]
    out["incrementFactor"] = value["increment_factor"]
    import capo_iot.types.rate_increase_criteria

    out["rateIncreaseCriteria"] = capo_iot.types.rate_increase_criteria.serialize_json(
        value["rate_increase_criteria"]
    )
    return out


def deserialize_json(data: dict) -> ExponentialRolloutRate:
    out: ExponentialRolloutRate = {}  # type: ignore[typeddict-item]
    if "baseRatePerMinute" in data:
        out["base_rate_per_minute"] = data["baseRatePerMinute"]
    else:
        raise DeserializationError(
            "ExponentialRolloutRate.base_rate_per_minute required"
        )
    if "incrementFactor" in data:
        out["increment_factor"] = data["incrementFactor"]
    else:
        raise DeserializationError("ExponentialRolloutRate.increment_factor required")
    if "rateIncreaseCriteria" in data:
        import capo_iot.types.rate_increase_criteria

        out["rate_increase_criteria"] = (
            capo_iot.types.rate_increase_criteria.deserialize_json(
                data["rateIncreaseCriteria"]
            )
        )
    else:
        raise DeserializationError(
            "ExponentialRolloutRate.rate_increase_criteria required"
        )
    return out
