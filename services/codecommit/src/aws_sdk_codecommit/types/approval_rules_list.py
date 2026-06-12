"""Generated from Smithy shape ``com.amazonaws.codecommit#ApprovalRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rule

ApprovalRulesList: TypeAlias = list[
    "aws_sdk_codecommit.types.approval_rule.ApprovalRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApprovalRulesList) -> list:
    import aws_sdk_codecommit.types.approval_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_codecommit.types.approval_rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ApprovalRulesList:
    import aws_sdk_codecommit.types.approval_rule

    out: ApprovalRulesList = []
    for item in data:
        out.append(
            aws_sdk_codecommit.types.approval_rule.deserialize_aws_json_1_1(item)
        )
    return out
