"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceCustomActionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.rule_group_source_custom_actions_details

RuleGroupSourceCustomActionsList: TypeAlias = list[
    "capo_securityhub.types.rule_group_source_custom_actions_details.RuleGroupSourceCustomActionsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupSourceCustomActionsList) -> list:
    import capo_securityhub.types.rule_group_source_custom_actions_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.rule_group_source_custom_actions_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RuleGroupSourceCustomActionsList:
    import capo_securityhub.types.rule_group_source_custom_actions_details

    out: RuleGroupSourceCustomActionsList = []
    for item in data:
        out.append(
            capo_securityhub.types.rule_group_source_custom_actions_details.deserialize_json(
                item
            )
        )
    return out
