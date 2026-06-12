"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceCustomActionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.rule_group_source_custom_actions_details

RuleGroupSourceCustomActionsList: TypeAlias = list[
    "aws_sdk_securityhub.types.rule_group_source_custom_actions_details.RuleGroupSourceCustomActionsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupSourceCustomActionsList) -> list:
    import aws_sdk_securityhub.types.rule_group_source_custom_actions_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.rule_group_source_custom_actions_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RuleGroupSourceCustomActionsList:
    import aws_sdk_securityhub.types.rule_group_source_custom_actions_details

    out: RuleGroupSourceCustomActionsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.rule_group_source_custom_actions_details.deserialize_json(
                item
            )
        )
    return out
