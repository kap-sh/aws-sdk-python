"""Generated from Smithy shape ``com.amazonaws.codecommit#ApprovalRulesNotSatisfiedList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.approval_rule_name

ApprovalRulesNotSatisfiedList: TypeAlias = list[
    "capo_codecommit.types.approval_rule_name.ApprovalRuleName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApprovalRulesNotSatisfiedList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ApprovalRulesNotSatisfiedList:
    return list(data)
