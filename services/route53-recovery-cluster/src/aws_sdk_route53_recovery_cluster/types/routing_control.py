"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#RoutingControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_cluster.types.arn
    import aws_sdk_route53_recovery_cluster.types.control_panel_name
    import aws_sdk_route53_recovery_cluster.types.owner
    import aws_sdk_route53_recovery_cluster.types.routing_control_name
    import aws_sdk_route53_recovery_cluster.types.routing_control_state


class RoutingControl(TypedDict, closed=True):
    control_panel_arn: NotRequired["aws_sdk_route53_recovery_cluster.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the control panel where the routing control is located.</p>"""
    control_panel_name: NotRequired[
        "aws_sdk_route53_recovery_cluster.types.control_panel_name.ControlPanelName"
    ]
    """<p>The name of the control panel where the routing control is located. Only ASCII characters are supported for control panel names.</p>"""
    routing_control_arn: NotRequired["aws_sdk_route53_recovery_cluster.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the routing control.</p>"""
    routing_control_name: NotRequired[
        "aws_sdk_route53_recovery_cluster.types.routing_control_name.RoutingControlName"
    ]
    """<p>The name of the routing control.</p>"""
    routing_control_state: NotRequired[
        "aws_sdk_route53_recovery_cluster.types.routing_control_state.RoutingControlState"
    ]
    """<p>The current state of the routing control. When a routing control state is set to ON, traffic flows to a cell. When the state is set to OFF, traffic does not flow. </p>"""
    owner: NotRequired["aws_sdk_route53_recovery_cluster.types.owner.Owner"]
    """<p>The Amazon Web Services account ID of the routing control owner.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RoutingControl) -> dict:
    out: dict = {}
    if "control_panel_arn" in value:
        out["ControlPanelArn"] = value["control_panel_arn"]
    if "control_panel_name" in value:
        out["ControlPanelName"] = value["control_panel_name"]
    if "routing_control_arn" in value:
        out["RoutingControlArn"] = value["routing_control_arn"]
    if "routing_control_name" in value:
        out["RoutingControlName"] = value["routing_control_name"]
    if "routing_control_state" in value:
        import aws_sdk_route53_recovery_cluster.types.routing_control_state

        out["RoutingControlState"] = (
            aws_sdk_route53_recovery_cluster.types.routing_control_state.serialize_aws_json_1_0(
                value["routing_control_state"]
            )
        )
    if "owner" in value:
        out["Owner"] = value["owner"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RoutingControl:
    out: RoutingControl = {}  # type: ignore[typeddict-item]
    if "ControlPanelArn" in data:
        out["control_panel_arn"] = data["ControlPanelArn"]
    if "ControlPanelName" in data:
        out["control_panel_name"] = data["ControlPanelName"]
    if "RoutingControlArn" in data:
        out["routing_control_arn"] = data["RoutingControlArn"]
    if "RoutingControlName" in data:
        out["routing_control_name"] = data["RoutingControlName"]
    if "RoutingControlState" in data:
        import aws_sdk_route53_recovery_cluster.types.routing_control_state

        out["routing_control_state"] = (
            aws_sdk_route53_recovery_cluster.types.routing_control_state.deserialize_aws_json_1_0(
                data["RoutingControlState"]
            )
        )
    if "Owner" in data:
        out["owner"] = data["Owner"]
    return out
