"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#CreateSafetyRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s
    import capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s
    import capo_route53_recovery_control_config.types.new_assertion_rule
    import capo_route53_recovery_control_config.types.new_gating_rule


class CreateSafetyRuleRequest(TypedDict, closed=True):
    assertion_rule: NotRequired[
        "capo_route53_recovery_control_config.types.new_assertion_rule.NewAssertionRule"
    ]
    """<p>The assertion rule requested.</p>"""
    client_token: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min1_max64_pattern_s.__stringMin1Max64PatternS"
    ]
    """<p>A unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request with an action, specify a client token in the request.</p>"""
    gating_rule: NotRequired[
        "capo_route53_recovery_control_config.types.new_gating_rule.NewGatingRule"
    ]
    """<p>The gating rule requested.</p>"""
    tags: NotRequired[
        "capo_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.__mapOf__stringMin0Max256PatternS"
    ]
    """<p>The tags associated with the safety rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSafetyRuleRequest) -> dict:
    out: dict = {}
    if "assertion_rule" in value:
        import capo_route53_recovery_control_config.types.new_assertion_rule

        out["AssertionRule"] = (
            capo_route53_recovery_control_config.types.new_assertion_rule.serialize_json(
                value["assertion_rule"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "gating_rule" in value:
        import capo_route53_recovery_control_config.types.new_gating_rule

        out["GatingRule"] = (
            capo_route53_recovery_control_config.types.new_gating_rule.serialize_json(
                value["gating_rule"]
            )
        )
    if "tags" in value:
        import capo_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s

        out["Tags"] = (
            capo_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.serialize_json(
                value["tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSafetyRuleRequest:
    out: CreateSafetyRuleRequest = {}  # type: ignore[typeddict-item]
    if "AssertionRule" in data:
        import capo_route53_recovery_control_config.types.new_assertion_rule

        out["assertion_rule"] = (
            capo_route53_recovery_control_config.types.new_assertion_rule.deserialize_json(
                data["AssertionRule"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "GatingRule" in data:
        import capo_route53_recovery_control_config.types.new_gating_rule

        out["gating_rule"] = (
            capo_route53_recovery_control_config.types.new_gating_rule.deserialize_json(
                data["GatingRule"]
            )
        )
    if "Tags" in data:
        import capo_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s

        out["tags"] = (
            capo_route53_recovery_control_config.types.__map_of__string_min0_max256_pattern_s.deserialize_json(
                data["Tags"]
            )
        )
    return out
