"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#ListSafetyRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__string
    import aws_sdk_route53_recovery_control_config.types.max_results


class ListSafetyRulesRequest(TypedDict, closed=True):
    control_panel_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the control panel.</p>"""
    max_results: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.max_results.MaxResults"
    ]
    """<p>The number of objects that you want to return with this call.</p>"""
    next_token: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string.__string"
    ]
    """<p>The token that identifies which batch of results you want to see.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSafetyRulesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSafetyRulesRequest:
    out: ListSafetyRulesRequest = {}  # type: ignore[typeddict-item]
    return out
