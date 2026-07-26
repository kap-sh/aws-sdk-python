"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#DeleteSafetyRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__string


class DeleteSafetyRuleRequest(TypedDict, closed=True):
    safety_rule_arn: "capo_route53_recovery_control_config.types.__string.__string"
    """<p>The ARN of the safety rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSafetyRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSafetyRuleRequest:
    out: DeleteSafetyRuleRequest = {}  # type: ignore[typeddict-item]
    return out
