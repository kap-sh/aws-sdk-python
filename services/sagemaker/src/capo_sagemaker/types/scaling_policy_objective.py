"""Generated from Smithy shape ``com.amazonaws.sagemaker#ScalingPolicyObjective``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.integer


class ScalingPolicyObjective(TypedDict, closed=True):
    min_invocations_per_minute: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The minimum number of expected requests to your endpoint per minute.</p>"""
    max_invocations_per_minute: NotRequired["capo_sagemaker.types.integer.Integer"]
    """<p>The maximum number of expected requests to your endpoint per minute.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingPolicyObjective) -> dict:
    out: dict = {}
    if "min_invocations_per_minute" in value:
        out["MinInvocationsPerMinute"] = value["min_invocations_per_minute"]
    if "max_invocations_per_minute" in value:
        out["MaxInvocationsPerMinute"] = value["max_invocations_per_minute"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScalingPolicyObjective:
    out: ScalingPolicyObjective = {}  # type: ignore[typeddict-item]
    if "MinInvocationsPerMinute" in data:
        out["min_invocations_per_minute"] = data["MinInvocationsPerMinute"]
    if "MaxInvocationsPerMinute" in data:
        out["max_invocations_per_minute"] = data["MaxInvocationsPerMinute"]
    return out
