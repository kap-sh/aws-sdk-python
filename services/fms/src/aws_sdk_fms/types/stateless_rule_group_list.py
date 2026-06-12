"""Generated from Smithy shape ``com.amazonaws.fms#StatelessRuleGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.stateless_rule_group

StatelessRuleGroupList: TypeAlias = list[
    "aws_sdk_fms.types.stateless_rule_group.StatelessRuleGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatelessRuleGroupList) -> list:
    import aws_sdk_fms.types.stateless_rule_group

    out: list = []
    for item in value:
        out.append(aws_sdk_fms.types.stateless_rule_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StatelessRuleGroupList:
    import aws_sdk_fms.types.stateless_rule_group

    out: StatelessRuleGroupList = []
    for item in data:
        out.append(
            aws_sdk_fms.types.stateless_rule_group.deserialize_aws_json_1_1(item)
        )
    return out
