"""Generated from Smithy shape ``com.amazonaws.codecommit#ApprovalRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.approval_rule

ApprovalRulesList: TypeAlias = list["capo_codecommit.types.approval_rule.ApprovalRule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApprovalRulesList) -> list:
    import capo_codecommit.types.approval_rule

    out: list = []
    for item in value:
        out.append(capo_codecommit.types.approval_rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ApprovalRulesList:
    import capo_codecommit.types.approval_rule

    out: ApprovalRulesList = []
    for item in data:
        out.append(capo_codecommit.types.approval_rule.deserialize_aws_json_1_1(item))
    return out
