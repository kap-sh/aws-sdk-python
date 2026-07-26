"""Generated from Smithy shape ``com.amazonaws.codecommit#ApprovalRuleEventMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.approval_rule_content
    import capo_codecommit.types.approval_rule_id
    import capo_codecommit.types.approval_rule_name


class ApprovalRuleEventMetadata(TypedDict, closed=True):
    approval_rule_name: NotRequired[
        "capo_codecommit.types.approval_rule_name.ApprovalRuleName"
    ]
    """<p>The name of the approval rule.</p>"""
    approval_rule_id: NotRequired[
        "capo_codecommit.types.approval_rule_id.ApprovalRuleId"
    ]
    """<p>The system-generated ID of the approval rule.</p>"""
    approval_rule_content: NotRequired[
        "capo_codecommit.types.approval_rule_content.ApprovalRuleContent"
    ]
    """<p>The content of the approval rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApprovalRuleEventMetadata) -> dict:
    out: dict = {}
    if "approval_rule_name" in value:
        out["approvalRuleName"] = value["approval_rule_name"]
    if "approval_rule_id" in value:
        out["approvalRuleId"] = value["approval_rule_id"]
    if "approval_rule_content" in value:
        out["approvalRuleContent"] = value["approval_rule_content"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApprovalRuleEventMetadata:
    out: ApprovalRuleEventMetadata = {}  # type: ignore[typeddict-item]
    if "approvalRuleName" in data:
        out["approval_rule_name"] = data["approvalRuleName"]
    if "approvalRuleId" in data:
        out["approval_rule_id"] = data["approvalRuleId"]
    if "approvalRuleContent" in data:
        out["approval_rule_content"] = data["approvalRuleContent"]
    return out
