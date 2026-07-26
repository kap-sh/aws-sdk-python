"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#DescribeControlPanelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__string


class DescribeControlPanelRequest(TypedDict, closed=True):
    control_panel_arn: "capo_route53_recovery_control_config.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the control panel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeControlPanelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeControlPanelRequest:
    out: DescribeControlPanelRequest = {}  # type: ignore[typeddict-item]
    return out
