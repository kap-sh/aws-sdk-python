"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#CreateSafetyRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.assertion_rule
    import aws_sdk_route53_recovery_control_config.types.gating_rule


class CreateSafetyRuleResponse(TypedDict):
    assertion_rule: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.assertion_rule.AssertionRule"
    ]
    """<p>The assertion rule created.</p>"""
    gating_rule: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.gating_rule.GatingRule"
    ]
    """<p>The gating rule created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSafetyRuleResponse) -> dict:
    out: dict = {}
    if "assertion_rule" in value:
        import aws_sdk_route53_recovery_control_config.types.assertion_rule

        out["AssertionRule"] = (
            aws_sdk_route53_recovery_control_config.types.assertion_rule.serialize_json(
                value["assertion_rule"]
            )
        )
    if "gating_rule" in value:
        import aws_sdk_route53_recovery_control_config.types.gating_rule

        out["GatingRule"] = (
            aws_sdk_route53_recovery_control_config.types.gating_rule.serialize_json(
                value["gating_rule"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSafetyRuleResponse:
    out: CreateSafetyRuleResponse = {}  # type: ignore[typeddict-item]
    if "AssertionRule" in data:
        import aws_sdk_route53_recovery_control_config.types.assertion_rule

        out["assertion_rule"] = (
            aws_sdk_route53_recovery_control_config.types.assertion_rule.deserialize_json(
                data["AssertionRule"]
            )
        )
    if "GatingRule" in data:
        import aws_sdk_route53_recovery_control_config.types.gating_rule

        out["gating_rule"] = (
            aws_sdk_route53_recovery_control_config.types.gating_rule.deserialize_json(
                data["GatingRule"]
            )
        )
    return out
