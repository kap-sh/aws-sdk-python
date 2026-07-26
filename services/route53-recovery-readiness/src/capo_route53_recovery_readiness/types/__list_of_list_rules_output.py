"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#__listOfListRulesOutput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.list_rules_output

__listOfListRulesOutput: TypeAlias = list[
    "capo_route53_recovery_readiness.types.list_rules_output.ListRulesOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfListRulesOutput) -> list:
    import capo_route53_recovery_readiness.types.list_rules_output

    out: list = []
    for item in value:
        out.append(
            capo_route53_recovery_readiness.types.list_rules_output.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfListRulesOutput:
    import capo_route53_recovery_readiness.types.list_rules_output

    out: __listOfListRulesOutput = []
    for item in data:
        out.append(
            capo_route53_recovery_readiness.types.list_rules_output.deserialize_json(
                item
            )
        )
    return out
