"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#CreateRoutingControlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s
    import capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09


class CreateRoutingControlRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
    ]
    """<p>A unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request with an action, specify a client token in the request.</p>"""
    cluster_arn: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
    ]
    """<p>The Amazon Resource Name (ARN) of the cluster that includes the routing control.</p>"""
    control_panel_arn: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
    ]
    """<p>The Amazon Resource Name (ARN) of the control panel that includes the routing control.</p>"""
    routing_control_name: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
    ]
    """<p>The name of the routing control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRoutingControlRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "control_panel_arn" in value:
        out["ControlPanelArn"] = value["control_panel_arn"]
    if "routing_control_name" in value:
        out["RoutingControlName"] = value["routing_control_name"]
    return out


def deserialize_json(data: dict) -> CreateRoutingControlRequest:
    out: CreateRoutingControlRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "ControlPanelArn" in data:
        out["control_panel_arn"] = data["ControlPanelArn"]
    if "RoutingControlName" in data:
        out["routing_control_name"] = data["RoutingControlName"]
    return out
