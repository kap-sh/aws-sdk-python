"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#RoutingControl``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s
    import aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09
    import aws_sdk_route53_recovery_control_config.types.__string_min12_max12_pattern_d12
    import aws_sdk_route53_recovery_control_config.types.status


class RoutingControl(TypedDict):
    control_panel_arn: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
    ]
    """<p>The Amazon Resource Name (ARN) of the control panel that includes the routing control.</p>"""
    name: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
    ]
    """<p>The name of the routing control.</p>"""
    routing_control_arn: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
    ]
    """<p>The Amazon Resource Name (ARN) of the routing control.</p>"""
    status: NotRequired["aws_sdk_route53_recovery_control_config.types.status.Status"]
    """<p>The deployment status of a routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.</p>"""
    owner: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string_min12_max12_pattern_d12.__stringMin12Max12PatternD12"
    ]
    """<p>The Amazon Web Services account ID of the routing control owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingControl) -> dict:
    out: dict = {}
    if "control_panel_arn" in value:
        out["ControlPanelArn"] = value["control_panel_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "routing_control_arn" in value:
        out["RoutingControlArn"] = value["routing_control_arn"]
    if "status" in value:
        import aws_sdk_route53_recovery_control_config.types.status

        out["Status"] = (
            aws_sdk_route53_recovery_control_config.types.status.serialize_json(
                value["status"]
            )
        )
    if "owner" in value:
        out["Owner"] = value["owner"]
    return out


def deserialize_json(data: dict) -> RoutingControl:
    out: RoutingControl = {}  # type: ignore[typeddict-item]
    if "ControlPanelArn" in data:
        out["control_panel_arn"] = data["ControlPanelArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "RoutingControlArn" in data:
        out["routing_control_arn"] = data["RoutingControlArn"]
    if "Status" in data:
        import aws_sdk_route53_recovery_control_config.types.status

        out["status"] = (
            aws_sdk_route53_recovery_control_config.types.status.deserialize_json(
                data["Status"]
            )
        )
    if "Owner" in data:
        out["owner"] = data["Owner"]
    return out
