"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#DescribeSafetyRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__string


class DescribeSafetyRuleRequest(TypedDict, closed=True):
    safety_rule_arn: "aws_sdk_route53_recovery_control_config.types.__string.__string"
    """<p>The ARN of the safety rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSafetyRuleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeSafetyRuleRequest:
    out: DescribeSafetyRuleRequest = {}  # type: ignore[typeddict-item]
    return out
