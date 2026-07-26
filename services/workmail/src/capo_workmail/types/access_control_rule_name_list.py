"""Generated from Smithy shape ``com.amazonaws.workmail#AccessControlRuleNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.access_control_rule_name

AccessControlRuleNameList: TypeAlias = list[
    "capo_workmail.types.access_control_rule_name.AccessControlRuleName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessControlRuleNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AccessControlRuleNameList:
    return list(data)
