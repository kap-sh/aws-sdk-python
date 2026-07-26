"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#ListControlPanelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__list_of_control_panel
    import capo_route53_recovery_control_config.types.__string_min1_max8096_pattern_s


class ListControlPanelsResponse(TypedDict, closed=True):
    control_panels: NotRequired[
        "capo_route53_recovery_control_config.types.__list_of_control_panel.__listOfControlPanel"
    ]
    """<p>The result of a successful ListControlPanel request.</p>"""
    next_token: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min1_max8096_pattern_s.__stringMin1Max8096PatternS"
    ]
    """<p>The token that identifies which batch of results you want to see.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListControlPanelsResponse) -> dict:
    out: dict = {}
    if "control_panels" in value:
        import capo_route53_recovery_control_config.types.__list_of_control_panel

        out["ControlPanels"] = (
            capo_route53_recovery_control_config.types.__list_of_control_panel.serialize_json(
                value["control_panels"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListControlPanelsResponse:
    out: ListControlPanelsResponse = {}  # type: ignore[typeddict-item]
    if "ControlPanels" in data:
        import capo_route53_recovery_control_config.types.__list_of_control_panel

        out["control_panels"] = (
            capo_route53_recovery_control_config.types.__list_of_control_panel.deserialize_json(
                data["ControlPanels"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
