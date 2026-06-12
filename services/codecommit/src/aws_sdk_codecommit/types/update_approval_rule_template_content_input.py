"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdateApprovalRuleTemplateContentInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rule_template_content
    import aws_sdk_codecommit.types.approval_rule_template_name
    import aws_sdk_codecommit.types.rule_content_sha256


class UpdateApprovalRuleTemplateContentInput(TypedDict):
    approval_rule_template_name: (
        "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName"
    )
    """<p>The name of the approval rule template where you want to update the content of the rule. </p>"""
    new_rule_content: "aws_sdk_codecommit.types.approval_rule_template_content.ApprovalRuleTemplateContent"
    """<p>The content that replaces the existing content of the rule. Content statements must be complete. You cannot provide only the changes.</p>"""
    existing_rule_content_sha256: NotRequired[
        "aws_sdk_codecommit.types.rule_content_sha256.RuleContentSha256"
    ]
    """<p>The SHA-256 hash signature for the content of the approval rule. You can retrieve this information by using <a>GetPullRequest</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApprovalRuleTemplateContentInput) -> dict:
    out: dict = {}
    out["approvalRuleTemplateName"] = value["approval_rule_template_name"]
    out["newRuleContent"] = value["new_rule_content"]
    if "existing_rule_content_sha256" in value:
        out["existingRuleContentSha256"] = value["existing_rule_content_sha256"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApprovalRuleTemplateContentInput:
    out: UpdateApprovalRuleTemplateContentInput = {}  # type: ignore[typeddict-item]
    if "approvalRuleTemplateName" in data:
        out["approval_rule_template_name"] = data["approvalRuleTemplateName"]
    else:
        raise DeserializationError(
            "UpdateApprovalRuleTemplateContentInput.approval_rule_template_name required"
        )
    if "newRuleContent" in data:
        out["new_rule_content"] = data["newRuleContent"]
    else:
        raise DeserializationError(
            "UpdateApprovalRuleTemplateContentInput.new_rule_content required"
        )
    if "existingRuleContentSha256" in data:
        out["existing_rule_content_sha256"] = data["existingRuleContentSha256"]
    return out
