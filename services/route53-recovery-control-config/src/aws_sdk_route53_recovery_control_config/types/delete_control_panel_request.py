"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#DeleteControlPanelRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__string


class DeleteControlPanelRequest(TypedDict):
    control_panel_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the control panel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteControlPanelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteControlPanelRequest:
    out: DeleteControlPanelRequest = {}  # type: ignore[typeddict-item]
    return out
