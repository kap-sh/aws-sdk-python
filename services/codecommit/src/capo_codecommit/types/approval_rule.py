"""Generated from Smithy shape ``com.amazonaws.codecommit#ApprovalRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.approval_rule_content
    import capo_codecommit.types.approval_rule_id
    import capo_codecommit.types.approval_rule_name
    import capo_codecommit.types.arn
    import capo_codecommit.types.creation_date
    import capo_codecommit.types.last_modified_date
    import capo_codecommit.types.origin_approval_rule_template
    import capo_codecommit.types.rule_content_sha256


class ApprovalRule(TypedDict, closed=True):
    approval_rule_id: NotRequired[
        "capo_codecommit.types.approval_rule_id.ApprovalRuleId"
    ]
    """<p>The system-generated ID of the approval rule.</p>"""
    approval_rule_name: NotRequired[
        "capo_codecommit.types.approval_rule_name.ApprovalRuleName"
    ]
    """<p>The name of the approval rule.</p>"""
    approval_rule_content: NotRequired[
        "capo_codecommit.types.approval_rule_content.ApprovalRuleContent"
    ]
    """<p>The content of the approval rule.</p>"""
    rule_content_sha256: NotRequired[
        "capo_codecommit.types.rule_content_sha256.RuleContentSha256"
    ]
    """<p>The SHA-256 hash signature for the content of the approval rule.</p>"""
    last_modified_date: NotRequired[
        "capo_codecommit.types.last_modified_date.LastModifiedDate"
    ]
    """<p>The date the approval rule was most recently changed, in timestamp format.</p>"""
    creation_date: NotRequired["capo_codecommit.types.creation_date.CreationDate"]
    """<p>The date the approval rule was created, in timestamp format.</p>"""
    last_modified_user: NotRequired["capo_codecommit.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the user who made the most recent changes to the approval rule.</p>"""
    origin_approval_rule_template: NotRequired[
        "capo_codecommit.types.origin_approval_rule_template.OriginApprovalRuleTemplate"
    ]
    """<p>The approval rule template used to create the rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApprovalRule) -> dict:
    out: dict = {}
    if "approval_rule_id" in value:
        out["approvalRuleId"] = value["approval_rule_id"]
    if "approval_rule_name" in value:
        out["approvalRuleName"] = value["approval_rule_name"]
    if "approval_rule_content" in value:
        out["approvalRuleContent"] = value["approval_rule_content"]
    if "rule_content_sha256" in value:
        out["ruleContentSha256"] = value["rule_content_sha256"]
    if "last_modified_date" in value:
        import capo_codecommit.types.last_modified_date

        out["lastModifiedDate"] = (
            capo_codecommit.types.last_modified_date.serialize_aws_json_1_1(
                value["last_modified_date"]
            )
        )
    if "creation_date" in value:
        import capo_codecommit.types.creation_date

        out["creationDate"] = (
            capo_codecommit.types.creation_date.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    if "last_modified_user" in value:
        out["lastModifiedUser"] = value["last_modified_user"]
    if "origin_approval_rule_template" in value:
        import capo_codecommit.types.origin_approval_rule_template

        out["originApprovalRuleTemplate"] = (
            capo_codecommit.types.origin_approval_rule_template.serialize_aws_json_1_1(
                value["origin_approval_rule_template"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApprovalRule:
    out: ApprovalRule = {}  # type: ignore[typeddict-item]
    if "approvalRuleId" in data:
        out["approval_rule_id"] = data["approvalRuleId"]
    if "approvalRuleName" in data:
        out["approval_rule_name"] = data["approvalRuleName"]
    if "approvalRuleContent" in data:
        out["approval_rule_content"] = data["approvalRuleContent"]
    if "ruleContentSha256" in data:
        out["rule_content_sha256"] = data["ruleContentSha256"]
    if "lastModifiedDate" in data:
        import capo_codecommit.types.last_modified_date

        out["last_modified_date"] = (
            capo_codecommit.types.last_modified_date.deserialize_aws_json_1_1(
                data["lastModifiedDate"]
            )
        )
    if "creationDate" in data:
        import capo_codecommit.types.creation_date

        out["creation_date"] = (
            capo_codecommit.types.creation_date.deserialize_aws_json_1_1(
                data["creationDate"]
            )
        )
    if "lastModifiedUser" in data:
        out["last_modified_user"] = data["lastModifiedUser"]
    if "originApprovalRuleTemplate" in data:
        import capo_codecommit.types.origin_approval_rule_template

        out["origin_approval_rule_template"] = (
            capo_codecommit.types.origin_approval_rule_template.deserialize_aws_json_1_1(
                data["originApprovalRuleTemplate"]
            )
        )
    return out
