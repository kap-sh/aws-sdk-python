"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatefulRulesOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.rule_group_source_stateful_rules_options_details

RuleGroupSourceStatefulRulesOptionsList: TypeAlias = list[
    "aws_sdk_securityhub.types.rule_group_source_stateful_rules_options_details.RuleGroupSourceStatefulRulesOptionsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupSourceStatefulRulesOptionsList) -> list:
    import aws_sdk_securityhub.types.rule_group_source_stateful_rules_options_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.rule_group_source_stateful_rules_options_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RuleGroupSourceStatefulRulesOptionsList:
    import aws_sdk_securityhub.types.rule_group_source_stateful_rules_options_details

    out: RuleGroupSourceStatefulRulesOptionsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.rule_group_source_stateful_rules_options_details.deserialize_json(
                item
            )
        )
    return out
