"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#UpdateSafetyRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.assertion_rule_update
    import aws_sdk_route53_recovery_control_config.types.gating_rule_update


class UpdateSafetyRuleRequest(TypedDict):
    assertion_rule_update: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.assertion_rule_update.AssertionRuleUpdate"
    ]
    """<p>The assertion rule to update.</p>"""
    gating_rule_update: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.gating_rule_update.GatingRuleUpdate"
    ]
    """<p>The gating rule to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSafetyRuleRequest) -> dict:
    out: dict = {}
    if "assertion_rule_update" in value:
        import aws_sdk_route53_recovery_control_config.types.assertion_rule_update

        out["AssertionRuleUpdate"] = (
            aws_sdk_route53_recovery_control_config.types.assertion_rule_update.serialize_json(
                value["assertion_rule_update"]
            )
        )
    if "gating_rule_update" in value:
        import aws_sdk_route53_recovery_control_config.types.gating_rule_update

        out["GatingRuleUpdate"] = (
            aws_sdk_route53_recovery_control_config.types.gating_rule_update.serialize_json(
                value["gating_rule_update"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSafetyRuleRequest:
    out: UpdateSafetyRuleRequest = {}  # type: ignore[typeddict-item]
    if "AssertionRuleUpdate" in data:
        import aws_sdk_route53_recovery_control_config.types.assertion_rule_update

        out["assertion_rule_update"] = (
            aws_sdk_route53_recovery_control_config.types.assertion_rule_update.deserialize_json(
                data["AssertionRuleUpdate"]
            )
        )
    if "GatingRuleUpdate" in data:
        import aws_sdk_route53_recovery_control_config.types.gating_rule_update

        out["gating_rule_update"] = (
            aws_sdk_route53_recovery_control_config.types.gating_rule_update.deserialize_json(
                data["GatingRuleUpdate"]
            )
        )
    return out
