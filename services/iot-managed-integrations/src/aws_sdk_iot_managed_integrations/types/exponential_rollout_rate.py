"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ExponentialRolloutRate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.base_rate_per_minute
    import aws_sdk_iot_managed_integrations.types.increment_factor
    import aws_sdk_iot_managed_integrations.types.rollout_rate_increase_criteria


class ExponentialRolloutRate(TypedDict, closed=True):
    base_rate_per_minute: NotRequired[
        "aws_sdk_iot_managed_integrations.types.base_rate_per_minute.BaseRatePerMinute"
    ]
    """<p>The base rate per minute for the rollout of an over-the-air (OTA) task.</p>"""
    increment_factor: NotRequired[
        "aws_sdk_iot_managed_integrations.types.increment_factor.IncrementFactor"
    ]
    """<p>The incremental factor for increasing the rollout rate of an over-the-air (OTA) task.</p>"""
    rate_increase_criteria: NotRequired[
        "aws_sdk_iot_managed_integrations.types.rollout_rate_increase_criteria.RolloutRateIncreaseCriteria"
    ]
    """<p>The criteria for increasing the rollout rate of an over-the-air (OTA) task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExponentialRolloutRate) -> dict:
    out: dict = {}
    if "base_rate_per_minute" in value:
        out["BaseRatePerMinute"] = value["base_rate_per_minute"]
    if "increment_factor" in value:
        out["IncrementFactor"] = value["increment_factor"]
    if "rate_increase_criteria" in value:
        import aws_sdk_iot_managed_integrations.types.rollout_rate_increase_criteria

        out["RateIncreaseCriteria"] = (
            aws_sdk_iot_managed_integrations.types.rollout_rate_increase_criteria.serialize_json(
                value["rate_increase_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExponentialRolloutRate:
    out: ExponentialRolloutRate = {}  # type: ignore[typeddict-item]
    if "BaseRatePerMinute" in data:
        out["base_rate_per_minute"] = data["BaseRatePerMinute"]
    if "IncrementFactor" in data:
        out["increment_factor"] = data["IncrementFactor"]
    if "RateIncreaseCriteria" in data:
        import aws_sdk_iot_managed_integrations.types.rollout_rate_increase_criteria

        out["rate_increase_criteria"] = (
            aws_sdk_iot_managed_integrations.types.rollout_rate_increase_criteria.deserialize_json(
                data["RateIncreaseCriteria"]
            )
        )
    return out
