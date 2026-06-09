"""Generated from Smithy shape ``com.amazonaws.eks#NodeRepairConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.boxed_boolean
    import aws_sdk_eks.types.node_repair_config_overrides_list
    import aws_sdk_eks.types.non_zero_integer
    import aws_sdk_eks.types.percent_capacity


class NodeRepairConfig(TypedDict):
    enabled: NotRequired["aws_sdk_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Specifies whether to enable node auto repair for the node group. Node auto repair is disabled by default.</p>"""
    max_unhealthy_node_threshold_count: NotRequired[
        "aws_sdk_eks.types.non_zero_integer.NonZeroInteger"
    ]
    """<p>Specify a count threshold of unhealthy nodes, above which node auto repair actions will stop. When using this, you cannot also set <code>maxUnhealthyNodeThresholdPercentage</code> at the same time.</p>"""
    max_unhealthy_node_threshold_percentage: NotRequired[
        "aws_sdk_eks.types.percent_capacity.PercentCapacity"
    ]
    """<p>Specify a percentage threshold of unhealthy nodes, above which node auto repair actions will stop. When using this, you cannot also set <code>maxUnhealthyNodeThresholdCount</code> at the same time.</p>"""
    max_parallel_nodes_repaired_count: NotRequired[
        "aws_sdk_eks.types.non_zero_integer.NonZeroInteger"
    ]
    """<p>Specify the maximum number of nodes that can be repaired concurrently or in parallel, expressed as a count of unhealthy nodes. This gives you finer-grained control over the pace of node replacements. When using this, you cannot also set <code>maxParallelNodesRepairedPercentage</code> at the same time.</p>"""
    max_parallel_nodes_repaired_percentage: NotRequired[
        "aws_sdk_eks.types.percent_capacity.PercentCapacity"
    ]
    """<p>Specify the maximum number of nodes that can be repaired concurrently or in parallel, expressed as a percentage of unhealthy nodes. This gives you finer-grained control over the pace of node replacements. When using this, you cannot also set <code>maxParallelNodesRepairedCount</code> at the same time.</p>"""
    node_repair_config_overrides: NotRequired[
        "aws_sdk_eks.types.node_repair_config_overrides_list.NodeRepairConfigOverridesList"
    ]
    """<p>Specify granular overrides for specific repair actions. These overrides control the repair action and the repair delay time before a node is considered eligible for repair. If you use this, you must specify all the values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeRepairConfig) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "max_unhealthy_node_threshold_count" in value:
        out["maxUnhealthyNodeThresholdCount"] = value[
            "max_unhealthy_node_threshold_count"
        ]
    if "max_unhealthy_node_threshold_percentage" in value:
        out["maxUnhealthyNodeThresholdPercentage"] = value[
            "max_unhealthy_node_threshold_percentage"
        ]
    if "max_parallel_nodes_repaired_count" in value:
        out["maxParallelNodesRepairedCount"] = value[
            "max_parallel_nodes_repaired_count"
        ]
    if "max_parallel_nodes_repaired_percentage" in value:
        out["maxParallelNodesRepairedPercentage"] = value[
            "max_parallel_nodes_repaired_percentage"
        ]
    if "node_repair_config_overrides" in value:
        import aws_sdk_eks.types.node_repair_config_overrides_list

        out["nodeRepairConfigOverrides"] = (
            aws_sdk_eks.types.node_repair_config_overrides_list.serialize_json(
                value["node_repair_config_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> NodeRepairConfig:
    out: NodeRepairConfig = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "maxUnhealthyNodeThresholdCount" in data:
        out["max_unhealthy_node_threshold_count"] = data[
            "maxUnhealthyNodeThresholdCount"
        ]
    if "maxUnhealthyNodeThresholdPercentage" in data:
        out["max_unhealthy_node_threshold_percentage"] = data[
            "maxUnhealthyNodeThresholdPercentage"
        ]
    if "maxParallelNodesRepairedCount" in data:
        out["max_parallel_nodes_repaired_count"] = data["maxParallelNodesRepairedCount"]
    if "maxParallelNodesRepairedPercentage" in data:
        out["max_parallel_nodes_repaired_percentage"] = data[
            "maxParallelNodesRepairedPercentage"
        ]
    if "nodeRepairConfigOverrides" in data:
        import aws_sdk_eks.types.node_repair_config_overrides_list

        out["node_repair_config_overrides"] = (
            aws_sdk_eks.types.node_repair_config_overrides_list.deserialize_json(
                data["nodeRepairConfigOverrides"]
            )
        )
    return out
