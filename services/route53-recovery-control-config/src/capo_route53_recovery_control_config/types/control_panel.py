"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#ControlPanel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__boolean
    import capo_route53_recovery_control_config.types.__integer
    import capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s
    import capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09
    import capo_route53_recovery_control_config.types.__string_min12_max12_pattern_d12
    import capo_route53_recovery_control_config.types.status


class ControlPanel(TypedDict, closed=True):
    cluster_arn: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
    ]
    """<p>The Amazon Resource Name (ARN) of the cluster that includes the control panel.</p>"""
    control_panel_arn: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
    ]
    """<p>The Amazon Resource Name (ARN) of the control panel.</p>"""
    default_control_panel: NotRequired[
        "capo_route53_recovery_control_config.types.__boolean.__boolean"
    ]
    """<p>A flag that Amazon Route 53 Application Recovery Controller sets to true to designate the default control panel for a cluster. When you create a cluster, Amazon Route 53 Application Recovery Controller creates a control panel, and sets this flag for that control panel. If you create a control panel yourself, this flag is set to false.</p>"""
    name: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
    ]
    """<p>The name of the control panel. You can use any non-white space character in the name.</p>"""
    routing_control_count: NotRequired[
        "capo_route53_recovery_control_config.types.__integer.__integer"
    ]
    """<p>The number of routing controls in the control panel.</p>"""
    status: NotRequired["capo_route53_recovery_control_config.types.status.Status"]
    """<p>The deployment status of control panel. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.</p>"""
    owner: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min12_max12_pattern_d12.__stringMin12Max12PatternD12"
    ]
    """<p>The Amazon Web Services account ID of the control panel owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlPanel) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "control_panel_arn" in value:
        out["ControlPanelArn"] = value["control_panel_arn"]
    if "default_control_panel" in value:
        out["DefaultControlPanel"] = value["default_control_panel"]
    if "name" in value:
        out["Name"] = value["name"]
    if "routing_control_count" in value:
        out["RoutingControlCount"] = value["routing_control_count"]
    if "status" in value:
        import capo_route53_recovery_control_config.types.status

        out["Status"] = (
            capo_route53_recovery_control_config.types.status.serialize_json(
                value["status"]
            )
        )
    if "owner" in value:
        out["Owner"] = value["owner"]
    return out


def deserialize_json(data: dict) -> ControlPanel:
    out: ControlPanel = {}  # type: ignore[typeddict-item]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "ControlPanelArn" in data:
        out["control_panel_arn"] = data["ControlPanelArn"]
    if "DefaultControlPanel" in data:
        out["default_control_panel"] = data["DefaultControlPanel"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "RoutingControlCount" in data:
        out["routing_control_count"] = data["RoutingControlCount"]
    if "Status" in data:
        import capo_route53_recovery_control_config.types.status

        out["status"] = (
            capo_route53_recovery_control_config.types.status.deserialize_json(
                data["Status"]
            )
        )
    if "Owner" in data:
        out["owner"] = data["Owner"]
    return out
