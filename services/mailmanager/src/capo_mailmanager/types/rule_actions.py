"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.rule_action

RuleActions: TypeAlias = list["capo_mailmanager.types.rule_action.RuleAction"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleActions) -> list:
    import capo_mailmanager.types.rule_action

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.rule_action.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> RuleActions:
    import capo_mailmanager.types.rule_action

    out: RuleActions = []
    for item in data:
        out.append(capo_mailmanager.types.rule_action.deserialize_aws_json_1_0(item))
    return out
