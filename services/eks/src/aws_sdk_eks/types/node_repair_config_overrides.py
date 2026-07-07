"""Generated from Smithy shape ``com.amazonaws.eks#NodeRepairConfigOverrides``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.non_zero_integer
    import aws_sdk_eks.types.repair_action
    import aws_sdk_eks.types.string


class NodeRepairConfigOverrides(TypedDict, closed=True):
    node_monitoring_condition: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>Specify an unhealthy condition reported by the node monitoring agent that this override would apply to.</p>"""
    node_unhealthy_reason: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>Specify a reason reported by the node monitoring agent that this override would apply to.</p>"""
    min_repair_wait_time_mins: NotRequired[
        "aws_sdk_eks.types.non_zero_integer.NonZeroInteger"
    ]
    """<p>Specify the minimum time in minutes to wait before attempting to repair a node with this specific <code>nodeMonitoringCondition</code> and <code>nodeUnhealthyReason</code>.</p>"""
    repair_action: NotRequired["aws_sdk_eks.types.repair_action.RepairAction"]
    """<p>Specify the repair action to take for nodes when all of the specified conditions are met.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeRepairConfigOverrides) -> dict:
    out: dict = {}
    if "node_monitoring_condition" in value:
        out["nodeMonitoringCondition"] = value["node_monitoring_condition"]
    if "node_unhealthy_reason" in value:
        out["nodeUnhealthyReason"] = value["node_unhealthy_reason"]
    if "min_repair_wait_time_mins" in value:
        out["minRepairWaitTimeMins"] = value["min_repair_wait_time_mins"]
    if "repair_action" in value:
        import aws_sdk_eks.types.repair_action

        out["repairAction"] = aws_sdk_eks.types.repair_action.serialize_json(
            value["repair_action"]
        )
    return out


def deserialize_json(data: dict) -> NodeRepairConfigOverrides:
    out: NodeRepairConfigOverrides = {}  # type: ignore[typeddict-item]
    if "nodeMonitoringCondition" in data:
        out["node_monitoring_condition"] = data["nodeMonitoringCondition"]
    if "nodeUnhealthyReason" in data:
        out["node_unhealthy_reason"] = data["nodeUnhealthyReason"]
    if "minRepairWaitTimeMins" in data:
        out["min_repair_wait_time_mins"] = data["minRepairWaitTimeMins"]
    if "repairAction" in data:
        import aws_sdk_eks.types.repair_action

        out["repair_action"] = aws_sdk_eks.types.repair_action.deserialize_json(
            data["repairAction"]
        )
    return out
