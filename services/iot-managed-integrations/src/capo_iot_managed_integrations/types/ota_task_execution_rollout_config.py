"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaTaskExecutionRolloutConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.exponential_rollout_rate
    import capo_iot_managed_integrations.types.maximum_per_minute


class OtaTaskExecutionRolloutConfig(TypedDict, closed=True):
    exponential_rollout_rate: NotRequired[
        "capo_iot_managed_integrations.types.exponential_rollout_rate.ExponentialRolloutRate"
    ]
    """<p>Structure representing exponential rate of rollout for an over-the-air (OTA) task.</p>"""
    maximum_per_minute: NotRequired[
        "capo_iot_managed_integrations.types.maximum_per_minute.MaximumPerMinute"
    ]
    """<p>The maximum number of things that will be notified of a pending task, per minute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OtaTaskExecutionRolloutConfig) -> dict:
    out: dict = {}
    if "exponential_rollout_rate" in value:
        import capo_iot_managed_integrations.types.exponential_rollout_rate

        out["ExponentialRolloutRate"] = (
            capo_iot_managed_integrations.types.exponential_rollout_rate.serialize_json(
                value["exponential_rollout_rate"]
            )
        )
    if "maximum_per_minute" in value:
        out["MaximumPerMinute"] = value["maximum_per_minute"]
    return out


def deserialize_json(data: dict) -> OtaTaskExecutionRolloutConfig:
    out: OtaTaskExecutionRolloutConfig = {}  # type: ignore[typeddict-item]
    if "ExponentialRolloutRate" in data:
        import capo_iot_managed_integrations.types.exponential_rollout_rate

        out["exponential_rollout_rate"] = (
            capo_iot_managed_integrations.types.exponential_rollout_rate.deserialize_json(
                data["ExponentialRolloutRate"]
            )
        )
    if "MaximumPerMinute" in data:
        out["maximum_per_minute"] = data["MaximumPerMinute"]
    return out
