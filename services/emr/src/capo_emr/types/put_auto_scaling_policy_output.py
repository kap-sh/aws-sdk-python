"""Generated from Smithy shape ``com.amazonaws.emr#PutAutoScalingPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.arn_type
    import capo_emr.types.auto_scaling_policy_description
    import capo_emr.types.cluster_id
    import capo_emr.types.instance_group_id


class PutAutoScalingPolicyOutput(TypedDict, closed=True):
    cluster_id: NotRequired["capo_emr.types.cluster_id.ClusterId"]
    """<p>Specifies the ID of a cluster. The instance group to which the automatic scaling policy is applied is within this cluster.</p>"""
    instance_group_id: NotRequired["capo_emr.types.instance_group_id.InstanceGroupId"]
    """<p>Specifies the ID of the instance group to which the scaling policy is applied.</p>"""
    auto_scaling_policy: NotRequired[
        "capo_emr.types.auto_scaling_policy_description.AutoScalingPolicyDescription"
    ]
    """<p>The automatic scaling policy definition.</p>"""
    cluster_arn: NotRequired["capo_emr.types.arn_type.ArnType"]
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAutoScalingPolicyOutput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "instance_group_id" in value:
        out["InstanceGroupId"] = value["instance_group_id"]
    if "auto_scaling_policy" in value:
        import capo_emr.types.auto_scaling_policy_description

        out["AutoScalingPolicy"] = (
            capo_emr.types.auto_scaling_policy_description.serialize_aws_json_1_1(
                value["auto_scaling_policy"]
            )
        )
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAutoScalingPolicyOutput:
    out: PutAutoScalingPolicyOutput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "InstanceGroupId" in data:
        out["instance_group_id"] = data["InstanceGroupId"]
    if "AutoScalingPolicy" in data:
        import capo_emr.types.auto_scaling_policy_description

        out["auto_scaling_policy"] = (
            capo_emr.types.auto_scaling_policy_description.deserialize_aws_json_1_1(
                data["AutoScalingPolicy"]
            )
        )
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    return out
