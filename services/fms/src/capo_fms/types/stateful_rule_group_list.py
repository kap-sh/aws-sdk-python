"""Generated from Smithy shape ``com.amazonaws.fms#StatefulRuleGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.stateful_rule_group

StatefulRuleGroupList: TypeAlias = list[
    "capo_fms.types.stateful_rule_group.StatefulRuleGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatefulRuleGroupList) -> list:
    import capo_fms.types.stateful_rule_group

    out: list = []
    for item in value:
        out.append(capo_fms.types.stateful_rule_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StatefulRuleGroupList:
    import capo_fms.types.stateful_rule_group

    out: StatefulRuleGroupList = []
    for item in data:
        out.append(capo_fms.types.stateful_rule_group.deserialize_aws_json_1_1(item))
    return out
