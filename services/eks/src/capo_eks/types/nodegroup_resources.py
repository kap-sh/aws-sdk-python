"""Generated from Smithy shape ``com.amazonaws.eks#NodegroupResources``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.auto_scaling_group_list
    import capo_eks.types.string


class NodegroupResources(TypedDict, closed=True):
    auto_scaling_groups: NotRequired[
        "capo_eks.types.auto_scaling_group_list.AutoScalingGroupList"
    ]
    """<p>The Auto Scaling groups associated with the node group.</p>"""
    remote_access_security_group: NotRequired["capo_eks.types.string.String"]
    """<p>The remote access security group associated with the node group. This security group controls SSH access to the nodes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodegroupResources) -> dict:
    out: dict = {}
    if "auto_scaling_groups" in value:
        import capo_eks.types.auto_scaling_group_list

        out["autoScalingGroups"] = (
            capo_eks.types.auto_scaling_group_list.serialize_json(
                value["auto_scaling_groups"]
            )
        )
    if "remote_access_security_group" in value:
        out["remoteAccessSecurityGroup"] = value["remote_access_security_group"]
    return out


def deserialize_json(data: dict) -> NodegroupResources:
    out: NodegroupResources = {}  # type: ignore[typeddict-item]
    if "autoScalingGroups" in data:
        import capo_eks.types.auto_scaling_group_list

        out["auto_scaling_groups"] = (
            capo_eks.types.auto_scaling_group_list.deserialize_json(
                data["autoScalingGroups"]
            )
        )
    if "remoteAccessSecurityGroup" in data:
        out["remote_access_security_group"] = data["remoteAccessSecurityGroup"]
    return out
