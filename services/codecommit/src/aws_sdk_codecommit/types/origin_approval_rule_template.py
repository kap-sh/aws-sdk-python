"""Generated from Smithy shape ``com.amazonaws.codecommit#OriginApprovalRuleTemplate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rule_template_id
    import aws_sdk_codecommit.types.approval_rule_template_name


class OriginApprovalRuleTemplate(TypedDict):
    approval_rule_template_id: NotRequired[
        "aws_sdk_codecommit.types.approval_rule_template_id.ApprovalRuleTemplateId"
    ]
    """<p>The ID of the template that created the approval rule.</p>"""
    approval_rule_template_name: NotRequired[
        "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName"
    ]
    """<p>The name of the template that created the approval rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OriginApprovalRuleTemplate) -> dict:
    out: dict = {}
    if "approval_rule_template_id" in value:
        out["approvalRuleTemplateId"] = value["approval_rule_template_id"]
    if "approval_rule_template_name" in value:
        out["approvalRuleTemplateName"] = value["approval_rule_template_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OriginApprovalRuleTemplate:
    out: OriginApprovalRuleTemplate = {}  # type: ignore[typeddict-item]
    if "approvalRuleTemplateId" in data:
        out["approval_rule_template_id"] = data["approvalRuleTemplateId"]
    if "approvalRuleTemplateName" in data:
        out["approval_rule_template_name"] = data["approvalRuleTemplateName"]
    return out
