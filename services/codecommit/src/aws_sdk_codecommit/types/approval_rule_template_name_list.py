"""Generated from Smithy shape ``com.amazonaws.codecommit#ApprovalRuleTemplateNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rule_template_name

ApprovalRuleTemplateNameList: TypeAlias = list[
    "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApprovalRuleTemplateNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ApprovalRuleTemplateNameList:
    return list(data)
