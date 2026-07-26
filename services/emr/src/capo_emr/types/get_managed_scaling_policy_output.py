"""Generated from Smithy shape ``com.amazonaws.emr#GetManagedScalingPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.managed_scaling_policy


class GetManagedScalingPolicyOutput(TypedDict, closed=True):
    managed_scaling_policy: NotRequired[
        "capo_emr.types.managed_scaling_policy.ManagedScalingPolicy"
    ]
    """<p>Specifies the managed scaling policy that is attached to an Amazon EMR cluster. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetManagedScalingPolicyOutput) -> dict:
    out: dict = {}
    if "managed_scaling_policy" in value:
        import capo_emr.types.managed_scaling_policy

        out["ManagedScalingPolicy"] = (
            capo_emr.types.managed_scaling_policy.serialize_aws_json_1_1(
                value["managed_scaling_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetManagedScalingPolicyOutput:
    out: GetManagedScalingPolicyOutput = {}  # type: ignore[typeddict-item]
    if "ManagedScalingPolicy" in data:
        import capo_emr.types.managed_scaling_policy

        out["managed_scaling_policy"] = (
            capo_emr.types.managed_scaling_policy.deserialize_aws_json_1_1(
                data["ManagedScalingPolicy"]
            )
        )
    return out
