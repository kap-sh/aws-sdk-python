"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#UpdateControlPanelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s
    import capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09


class UpdateControlPanelRequest(TypedDict, closed=True):
    control_panel_arn: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min1_max256_pattern_a_za_z09.__stringMin1Max256PatternAZaZ09"
    ]
    """<p>The Amazon Resource Name (ARN) of the control panel.</p>"""
    control_panel_name: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
    ]
    """<p>The name of the control panel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateControlPanelRequest) -> dict:
    out: dict = {}
    if "control_panel_arn" in value:
        out["ControlPanelArn"] = value["control_panel_arn"]
    if "control_panel_name" in value:
        out["ControlPanelName"] = value["control_panel_name"]
    return out


def deserialize_json(data: dict) -> UpdateControlPanelRequest:
    out: UpdateControlPanelRequest = {}  # type: ignore[typeddict-item]
    if "ControlPanelArn" in data:
        out["control_panel_arn"] = data["ControlPanelArn"]
    if "ControlPanelName" in data:
        out["control_panel_name"] = data["ControlPanelName"]
    return out
