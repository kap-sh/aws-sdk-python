"""Generated from Smithy shape ``com.amazonaws.eks#UpdateNodegroupConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.node_repair_config
    import aws_sdk_eks.types.nodegroup_scaling_config
    import aws_sdk_eks.types.nodegroup_update_config
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.update_labels_payload
    import aws_sdk_eks.types.update_taints_payload
    import aws_sdk_eks.types.warm_pool_config


class UpdateNodegroupConfigRequest(TypedDict):
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    nodegroup_name: "aws_sdk_eks.types.string.String"
    """<p>The name of the managed node group to update.</p>"""
    labels: NotRequired["aws_sdk_eks.types.update_labels_payload.UpdateLabelsPayload"]
    """<p>The Kubernetes <code>labels</code> to apply to the nodes in the node group after the update.</p>"""
    taints: NotRequired["aws_sdk_eks.types.update_taints_payload.UpdateTaintsPayload"]
    """<p>The Kubernetes taints to be applied to the nodes in the node group after the update. For more information, see <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html\">Node taints on managed node groups</a>.</p>"""
    scaling_config: NotRequired[
        "aws_sdk_eks.types.nodegroup_scaling_config.NodegroupScalingConfig"
    ]
    """<p>The scaling configuration details for the Auto Scaling group after the update.</p>"""
    update_config: NotRequired[
        "aws_sdk_eks.types.nodegroup_update_config.NodegroupUpdateConfig"
    ]
    """<p>The node group update configuration.</p>"""
    node_repair_config: NotRequired[
        "aws_sdk_eks.types.node_repair_config.NodeRepairConfig"
    ]
    """<p>The node auto repair configuration for the node group.</p>"""
    warm_pool_config: NotRequired["aws_sdk_eks.types.warm_pool_config.WarmPoolConfig"]
    """<p>The warm pool configuration to apply to the node group. You can use this to add a warm pool to an existing node group or modify the settings of an existing warm pool.</p>"""
    client_request_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNodegroupConfigRequest) -> dict:
    out: dict = {}
    if "labels" in value:
        import aws_sdk_eks.types.update_labels_payload

        out["labels"] = aws_sdk_eks.types.update_labels_payload.serialize_json(
            value["labels"]
        )
    if "taints" in value:
        import aws_sdk_eks.types.update_taints_payload

        out["taints"] = aws_sdk_eks.types.update_taints_payload.serialize_json(
            value["taints"]
        )
    if "scaling_config" in value:
        import aws_sdk_eks.types.nodegroup_scaling_config

        out["scalingConfig"] = (
            aws_sdk_eks.types.nodegroup_scaling_config.serialize_json(
                value["scaling_config"]
            )
        )
    if "update_config" in value:
        import aws_sdk_eks.types.nodegroup_update_config

        out["updateConfig"] = aws_sdk_eks.types.nodegroup_update_config.serialize_json(
            value["update_config"]
        )
    if "node_repair_config" in value:
        import aws_sdk_eks.types.node_repair_config

        out["nodeRepairConfig"] = aws_sdk_eks.types.node_repair_config.serialize_json(
            value["node_repair_config"]
        )
    if "warm_pool_config" in value:
        import aws_sdk_eks.types.warm_pool_config

        out["warmPoolConfig"] = aws_sdk_eks.types.warm_pool_config.serialize_json(
            value["warm_pool_config"]
        )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> UpdateNodegroupConfigRequest:
    out: UpdateNodegroupConfigRequest = {}  # type: ignore[typeddict-item]
    if "labels" in data:
        import aws_sdk_eks.types.update_labels_payload

        out["labels"] = aws_sdk_eks.types.update_labels_payload.deserialize_json(
            data["labels"]
        )
    if "taints" in data:
        import aws_sdk_eks.types.update_taints_payload

        out["taints"] = aws_sdk_eks.types.update_taints_payload.deserialize_json(
            data["taints"]
        )
    if "scalingConfig" in data:
        import aws_sdk_eks.types.nodegroup_scaling_config

        out["scaling_config"] = (
            aws_sdk_eks.types.nodegroup_scaling_config.deserialize_json(
                data["scalingConfig"]
            )
        )
    if "updateConfig" in data:
        import aws_sdk_eks.types.nodegroup_update_config

        out["update_config"] = (
            aws_sdk_eks.types.nodegroup_update_config.deserialize_json(
                data["updateConfig"]
            )
        )
    if "nodeRepairConfig" in data:
        import aws_sdk_eks.types.node_repair_config

        out["node_repair_config"] = (
            aws_sdk_eks.types.node_repair_config.deserialize_json(
                data["nodeRepairConfig"]
            )
        )
    if "warmPoolConfig" in data:
        import aws_sdk_eks.types.warm_pool_config

        out["warm_pool_config"] = aws_sdk_eks.types.warm_pool_config.deserialize_json(
            data["warmPoolConfig"]
        )
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    return out
