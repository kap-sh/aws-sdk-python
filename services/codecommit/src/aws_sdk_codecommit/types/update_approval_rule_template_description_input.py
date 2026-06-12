"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdateApprovalRuleTemplateDescriptionInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rule_template_description
    import aws_sdk_codecommit.types.approval_rule_template_name


class UpdateApprovalRuleTemplateDescriptionInput(TypedDict):
    approval_rule_template_name: (
        "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName"
    )
    """<p>The name of the template for which you want to update the description.</p>"""
    approval_rule_template_description: "aws_sdk_codecommit.types.approval_rule_template_description.ApprovalRuleTemplateDescription"
    """<p>The updated description of the approval rule template.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApprovalRuleTemplateDescriptionInput) -> dict:
    out: dict = {}
    out["approvalRuleTemplateName"] = value["approval_rule_template_name"]
    out["approvalRuleTemplateDescription"] = value["approval_rule_template_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApprovalRuleTemplateDescriptionInput:
    out: UpdateApprovalRuleTemplateDescriptionInput = {}  # type: ignore[typeddict-item]
    if "approvalRuleTemplateName" in data:
        out["approval_rule_template_name"] = data["approvalRuleTemplateName"]
    else:
        raise DeserializationError(
            "UpdateApprovalRuleTemplateDescriptionInput.approval_rule_template_name required"
        )
    if "approvalRuleTemplateDescription" in data:
        out["approval_rule_template_description"] = data[
            "approvalRuleTemplateDescription"
        ]
    else:
        raise DeserializationError(
            "UpdateApprovalRuleTemplateDescriptionInput.approval_rule_template_description required"
        )
    return out
