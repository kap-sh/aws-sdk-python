"""Generated from Smithy shape ``com.amazonaws.emr#RemoveAutoScalingPolicyInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.cluster_id
    import aws_sdk_emr.types.instance_group_id


class RemoveAutoScalingPolicyInput(TypedDict):
    cluster_id: NotRequired["aws_sdk_emr.types.cluster_id.ClusterId"]
    """<p>Specifies the ID of a cluster. The instance group to which the automatic scaling policy is applied is within this cluster.</p>"""
    instance_group_id: NotRequired[
        "aws_sdk_emr.types.instance_group_id.InstanceGroupId"
    ]
    """<p>Specifies the ID of the instance group to which the scaling policy is applied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveAutoScalingPolicyInput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "instance_group_id" in value:
        out["InstanceGroupId"] = value["instance_group_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveAutoScalingPolicyInput:
    out: RemoveAutoScalingPolicyInput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "InstanceGroupId" in data:
        out["instance_group_id"] = data["InstanceGroupId"]
    return out
