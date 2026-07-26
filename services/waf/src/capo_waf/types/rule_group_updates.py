"""Generated from Smithy shape ``com.amazonaws.waf#RuleGroupUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf.types.rule_group_update

RuleGroupUpdates: TypeAlias = list["capo_waf.types.rule_group_update.RuleGroupUpdate"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleGroupUpdates) -> list:
    import capo_waf.types.rule_group_update

    out: list = []
    for item in value:
        out.append(capo_waf.types.rule_group_update.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RuleGroupUpdates:
    import capo_waf.types.rule_group_update

    out: RuleGroupUpdates = []
    for item in data:
        out.append(capo_waf.types.rule_group_update.deserialize_aws_json_1_1(item))
    return out
