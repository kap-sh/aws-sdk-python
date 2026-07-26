"""Generated from Smithy shape ``com.amazonaws.emr#PutAutoScalingPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.auto_scaling_policy
    import capo_emr.types.cluster_id
    import capo_emr.types.instance_group_id


class PutAutoScalingPolicyInput(TypedDict, closed=True):
    cluster_id: NotRequired["capo_emr.types.cluster_id.ClusterId"]
    """<p>Specifies the ID of a cluster. The instance group to which the automatic scaling policy is applied is within this cluster.</p>"""
    instance_group_id: NotRequired["capo_emr.types.instance_group_id.InstanceGroupId"]
    """<p>Specifies the ID of the instance group to which the automatic scaling policy is applied.</p>"""
    auto_scaling_policy: NotRequired[
        "capo_emr.types.auto_scaling_policy.AutoScalingPolicy"
    ]
    """<p>Specifies the definition of the automatic scaling policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAutoScalingPolicyInput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "instance_group_id" in value:
        out["InstanceGroupId"] = value["instance_group_id"]
    if "auto_scaling_policy" in value:
        import capo_emr.types.auto_scaling_policy

        out["AutoScalingPolicy"] = (
            capo_emr.types.auto_scaling_policy.serialize_aws_json_1_1(
                value["auto_scaling_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAutoScalingPolicyInput:
    out: PutAutoScalingPolicyInput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "InstanceGroupId" in data:
        out["instance_group_id"] = data["InstanceGroupId"]
    if "AutoScalingPolicy" in data:
        import capo_emr.types.auto_scaling_policy

        out["auto_scaling_policy"] = (
            capo_emr.types.auto_scaling_policy.deserialize_aws_json_1_1(
                data["AutoScalingPolicy"]
            )
        )
    return out
