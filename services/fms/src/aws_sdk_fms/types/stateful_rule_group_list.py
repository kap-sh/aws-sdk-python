"""Generated from Smithy shape ``com.amazonaws.fms#StatefulRuleGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.stateful_rule_group

StatefulRuleGroupList: TypeAlias = list[
    "aws_sdk_fms.types.stateful_rule_group.StatefulRuleGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatefulRuleGroupList) -> list:
    import aws_sdk_fms.types.stateful_rule_group

    out: list = []
    for item in value:
        out.append(aws_sdk_fms.types.stateful_rule_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StatefulRuleGroupList:
    import aws_sdk_fms.types.stateful_rule_group

    out: StatefulRuleGroupList = []
    for item in data:
        out.append(aws_sdk_fms.types.stateful_rule_group.deserialize_aws_json_1_1(item))
    return out
