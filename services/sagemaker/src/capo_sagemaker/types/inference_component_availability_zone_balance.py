"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentAvailabilityZoneBalance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.availability_zone_balance_enforcement_mode
    import capo_sagemaker.types.availability_zone_balance_max_imbalance


class InferenceComponentAvailabilityZoneBalance(TypedDict, closed=True):
    enforcement_mode: NotRequired[
        "capo_sagemaker.types.availability_zone_balance_enforcement_mode.AvailabilityZoneBalanceEnforcementMode"
    ]
    """<p>Determines how strictly the Availability Zone balance constraint is enforced.</p> <dl> <dt>PERMISSIVE</dt> <dd> <p>The endpoint attempts to balance copies across Availability Zones but proceeds with scheduling even if balance can't be achieved due to available capacity or instance distribution across Availability Zones.</p> </dd> </dl>"""
    max_imbalance: NotRequired[
        "capo_sagemaker.types.availability_zone_balance_max_imbalance.AvailabilityZoneBalanceMaxImbalance"
    ]
    """<p>The maximum allowed difference in the number of inference component copies between any two Availability Zones. This parameter applies only when the endpoint has instances across two or more Availability Zones. A copy placement is allowed if it reduces imbalance or the resulting imbalance is within this value.</p> <p>Default value: <code>0</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentAvailabilityZoneBalance) -> dict:
    out: dict = {}
    if "enforcement_mode" in value:
        import capo_sagemaker.types.availability_zone_balance_enforcement_mode

        out["EnforcementMode"] = (
            capo_sagemaker.types.availability_zone_balance_enforcement_mode.serialize_aws_json_1_1(
                value["enforcement_mode"]
            )
        )
    if "max_imbalance" in value:
        out["MaxImbalance"] = value["max_imbalance"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceComponentAvailabilityZoneBalance:
    out: InferenceComponentAvailabilityZoneBalance = {}  # type: ignore[typeddict-item]
    if "EnforcementMode" in data:
        import capo_sagemaker.types.availability_zone_balance_enforcement_mode

        out["enforcement_mode"] = (
            capo_sagemaker.types.availability_zone_balance_enforcement_mode.deserialize_aws_json_1_1(
                data["EnforcementMode"]
            )
        )
    if "MaxImbalance" in data:
        out["max_imbalance"] = data["MaxImbalance"]
    return out
