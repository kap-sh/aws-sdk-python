"""Generated from Smithy shape ``com.amazonaws.wafv2#RuleActionOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.rule_action_override

RuleActionOverrides: TypeAlias = list[
    "capo_wafv2.types.rule_action_override.RuleActionOverride"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleActionOverrides) -> list:
    import capo_wafv2.types.rule_action_override

    out: list = []
    for item in value:
        out.append(capo_wafv2.types.rule_action_override.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RuleActionOverrides:
    import capo_wafv2.types.rule_action_override

    out: RuleActionOverrides = []
    for item in data:
        out.append(capo_wafv2.types.rule_action_override.deserialize_aws_json_1_1(item))
    return out
