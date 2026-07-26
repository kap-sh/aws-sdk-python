"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#__listOfControlPanel``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.control_panel

__listOfControlPanel: TypeAlias = list[
    "capo_route53_recovery_control_config.types.control_panel.ControlPanel"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfControlPanel) -> list:
    import capo_route53_recovery_control_config.types.control_panel

    out: list = []
    for item in value:
        out.append(
            capo_route53_recovery_control_config.types.control_panel.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfControlPanel:
    import capo_route53_recovery_control_config.types.control_panel

    out: __listOfControlPanel = []
    for item in data:
        out.append(
            capo_route53_recovery_control_config.types.control_panel.deserialize_json(
                item
            )
        )
    return out
