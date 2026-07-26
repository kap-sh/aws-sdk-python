"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#UpdateSafetyRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.assertion_rule
    import capo_route53_recovery_control_config.types.gating_rule


class UpdateSafetyRuleResponse(TypedDict, closed=True):
    assertion_rule: NotRequired[
        "capo_route53_recovery_control_config.types.assertion_rule.AssertionRule"
    ]
    """<p>The assertion rule updated.</p>"""
    gating_rule: NotRequired[
        "capo_route53_recovery_control_config.types.gating_rule.GatingRule"
    ]
    """<p>The gating rule updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSafetyRuleResponse) -> dict:
    out: dict = {}
    if "assertion_rule" in value:
        import capo_route53_recovery_control_config.types.assertion_rule

        out["AssertionRule"] = (
            capo_route53_recovery_control_config.types.assertion_rule.serialize_json(
                value["assertion_rule"]
            )
        )
    if "gating_rule" in value:
        import capo_route53_recovery_control_config.types.gating_rule

        out["GatingRule"] = (
            capo_route53_recovery_control_config.types.gating_rule.serialize_json(
                value["gating_rule"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSafetyRuleResponse:
    out: UpdateSafetyRuleResponse = {}  # type: ignore[typeddict-item]
    if "AssertionRule" in data:
        import capo_route53_recovery_control_config.types.assertion_rule

        out["assertion_rule"] = (
            capo_route53_recovery_control_config.types.assertion_rule.deserialize_json(
                data["AssertionRule"]
            )
        )
    if "GatingRule" in data:
        import capo_route53_recovery_control_config.types.gating_rule

        out["gating_rule"] = (
            capo_route53_recovery_control_config.types.gating_rule.deserialize_json(
                data["GatingRule"]
            )
        )
    return out
