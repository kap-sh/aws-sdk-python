"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#UpdateControlPanelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.control_panel


class UpdateControlPanelResponse(TypedDict, closed=True):
    control_panel: NotRequired[
        "capo_route53_recovery_control_config.types.control_panel.ControlPanel"
    ]
    """<p>The control panel to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateControlPanelResponse) -> dict:
    out: dict = {}
    if "control_panel" in value:
        import capo_route53_recovery_control_config.types.control_panel

        out["ControlPanel"] = (
            capo_route53_recovery_control_config.types.control_panel.serialize_json(
                value["control_panel"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateControlPanelResponse:
    out: UpdateControlPanelResponse = {}  # type: ignore[typeddict-item]
    if "ControlPanel" in data:
        import capo_route53_recovery_control_config.types.control_panel

        out["control_panel"] = (
            capo_route53_recovery_control_config.types.control_panel.deserialize_json(
                data["ControlPanel"]
            )
        )
    return out
