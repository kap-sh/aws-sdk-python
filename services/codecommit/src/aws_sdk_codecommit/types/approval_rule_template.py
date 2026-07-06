"""Generated from Smithy shape ``com.amazonaws.codecommit#ApprovalRuleTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rule_template_content
    import aws_sdk_codecommit.types.approval_rule_template_description
    import aws_sdk_codecommit.types.approval_rule_template_id
    import aws_sdk_codecommit.types.approval_rule_template_name
    import aws_sdk_codecommit.types.arn
    import aws_sdk_codecommit.types.creation_date
    import aws_sdk_codecommit.types.last_modified_date
    import aws_sdk_codecommit.types.rule_content_sha256


class ApprovalRuleTemplate(TypedDict, closed=True):
    approval_rule_template_id: NotRequired[
        "aws_sdk_codecommit.types.approval_rule_template_id.ApprovalRuleTemplateId"
    ]
    """<p>The system-generated ID of the approval rule template.</p>"""
    approval_rule_template_name: NotRequired[
        "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName"
    ]
    """<p>The name of the approval rule template.</p>"""
    approval_rule_template_description: NotRequired[
        "aws_sdk_codecommit.types.approval_rule_template_description.ApprovalRuleTemplateDescription"
    ]
    """<p>The description of the approval rule template.</p>"""
    approval_rule_template_content: NotRequired[
        "aws_sdk_codecommit.types.approval_rule_template_content.ApprovalRuleTemplateContent"
    ]
    """<p>The content of the approval rule template.</p>"""
    rule_content_sha256: NotRequired[
        "aws_sdk_codecommit.types.rule_content_sha256.RuleContentSha256"
    ]
    """<p>The SHA-256 hash signature for the content of the approval rule template.</p>"""
    last_modified_date: NotRequired[
        "aws_sdk_codecommit.types.last_modified_date.LastModifiedDate"
    ]
    """<p>The date the approval rule template was most recently changed, in timestamp format.</p>"""
    creation_date: NotRequired["aws_sdk_codecommit.types.creation_date.CreationDate"]
    """<p>The date the approval rule template was created, in timestamp format.</p>"""
    last_modified_user: NotRequired["aws_sdk_codecommit.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule template.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApprovalRuleTemplate) -> dict:
    out: dict = {}
    if "approval_rule_template_id" in value:
        out["approvalRuleTemplateId"] = value["approval_rule_template_id"]
    if "approval_rule_template_name" in value:
        out["approvalRuleTemplateName"] = value["approval_rule_template_name"]
    if "approval_rule_template_description" in value:
        out["approvalRuleTemplateDescription"] = value[
            "approval_rule_template_description"
        ]
    if "approval_rule_template_content" in value:
        out["approvalRuleTemplateContent"] = value["approval_rule_template_content"]
    if "rule_content_sha256" in value:
        out["ruleContentSha256"] = value["rule_content_sha256"]
    if "last_modified_date" in value:
        import aws_sdk_codecommit.types.last_modified_date

        out["lastModifiedDate"] = (
            aws_sdk_codecommit.types.last_modified_date.serialize_aws_json_1_1(
                value["last_modified_date"]
            )
        )
    if "creation_date" in value:
        import aws_sdk_codecommit.types.creation_date

        out["creationDate"] = (
            aws_sdk_codecommit.types.creation_date.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    if "last_modified_user" in value:
        out["lastModifiedUser"] = value["last_modified_user"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApprovalRuleTemplate:
    out: ApprovalRuleTemplate = {}  # type: ignore[typeddict-item]
    if "approvalRuleTemplateId" in data:
        out["approval_rule_template_id"] = data["approvalRuleTemplateId"]
    if "approvalRuleTemplateName" in data:
        out["approval_rule_template_name"] = data["approvalRuleTemplateName"]
    if "approvalRuleTemplateDescription" in data:
        out["approval_rule_template_description"] = data[
            "approvalRuleTemplateDescription"
        ]
    if "approvalRuleTemplateContent" in data:
        out["approval_rule_template_content"] = data["approvalRuleTemplateContent"]
    if "ruleContentSha256" in data:
        out["rule_content_sha256"] = data["ruleContentSha256"]
    if "lastModifiedDate" in data:
        import aws_sdk_codecommit.types.last_modified_date

        out["last_modified_date"] = (
            aws_sdk_codecommit.types.last_modified_date.deserialize_aws_json_1_1(
                data["lastModifiedDate"]
            )
        )
    if "creationDate" in data:
        import aws_sdk_codecommit.types.creation_date

        out["creation_date"] = (
            aws_sdk_codecommit.types.creation_date.deserialize_aws_json_1_1(
                data["creationDate"]
            )
        )
    if "lastModifiedUser" in data:
        out["last_modified_user"] = data["lastModifiedUser"]
    return out
