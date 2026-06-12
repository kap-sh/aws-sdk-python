"""Generated from Smithy shape ``com.amazonaws.emr#PutManagedScalingPolicyInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.cluster_id
    import aws_sdk_emr.types.managed_scaling_policy


class PutManagedScalingPolicyInput(TypedDict):
    cluster_id: NotRequired["aws_sdk_emr.types.cluster_id.ClusterId"]
    """<p>Specifies the ID of an Amazon EMR cluster where the managed scaling policy is attached. </p>"""
    managed_scaling_policy: NotRequired[
        "aws_sdk_emr.types.managed_scaling_policy.ManagedScalingPolicy"
    ]
    """<p>Specifies the constraints for the managed scaling policy. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutManagedScalingPolicyInput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "managed_scaling_policy" in value:
        import aws_sdk_emr.types.managed_scaling_policy

        out["ManagedScalingPolicy"] = (
            aws_sdk_emr.types.managed_scaling_policy.serialize_aws_json_1_1(
                value["managed_scaling_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutManagedScalingPolicyInput:
    out: PutManagedScalingPolicyInput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "ManagedScalingPolicy" in data:
        import aws_sdk_emr.types.managed_scaling_policy

        out["managed_scaling_policy"] = (
            aws_sdk_emr.types.managed_scaling_policy.deserialize_aws_json_1_1(
                data["ManagedScalingPolicy"]
            )
        )
    return out
