"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#UpdateControlPanelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.control_panel


class UpdateControlPanelResponse(TypedDict):
    control_panel: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.control_panel.ControlPanel"
    ]
    """<p>The control panel to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateControlPanelResponse) -> dict:
    out: dict = {}
    if "control_panel" in value:
        import aws_sdk_route53_recovery_control_config.types.control_panel

        out["ControlPanel"] = (
            aws_sdk_route53_recovery_control_config.types.control_panel.serialize_json(
                value["control_panel"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateControlPanelResponse:
    out: UpdateControlPanelResponse = {}  # type: ignore[typeddict-item]
    if "ControlPanel" in data:
        import aws_sdk_route53_recovery_control_config.types.control_panel

        out["control_panel"] = (
            aws_sdk_route53_recovery_control_config.types.control_panel.deserialize_json(
                data["ControlPanel"]
            )
        )
    return out
