"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#__listOfRuleResult``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.rule_result

__listOfRuleResult: TypeAlias = list[
    "capo_route53_recovery_readiness.types.rule_result.RuleResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRuleResult) -> list:
    import capo_route53_recovery_readiness.types.rule_result

    out: list = []
    for item in value:
        out.append(
            capo_route53_recovery_readiness.types.rule_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfRuleResult:
    import capo_route53_recovery_readiness.types.rule_result

    out: __listOfRuleResult = []
    for item in data:
        out.append(
            capo_route53_recovery_readiness.types.rule_result.deserialize_json(item)
        )
    return out
