"""Generated from Smithy shape ``com.amazonaws.codecommit#DisassociateApprovalRuleTemplateFromRepositoryInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rule_template_name
    import aws_sdk_codecommit.types.repository_name


class DisassociateApprovalRuleTemplateFromRepositoryInput(TypedDict):
    approval_rule_template_name: (
        "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName"
    )
    """<p>The name of the approval rule template to disassociate from a specified repository.</p>"""
    repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository you want to disassociate from the template.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DisassociateApprovalRuleTemplateFromRepositoryInput,
) -> dict:
    out: dict = {}
    out["approvalRuleTemplateName"] = value["approval_rule_template_name"]
    out["repositoryName"] = value["repository_name"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DisassociateApprovalRuleTemplateFromRepositoryInput:
    out: DisassociateApprovalRuleTemplateFromRepositoryInput = {}  # type: ignore[typeddict-item]
    if "approvalRuleTemplateName" in data:
        out["approval_rule_template_name"] = data["approvalRuleTemplateName"]
    else:
        raise DeserializationError(
            "DisassociateApprovalRuleTemplateFromRepositoryInput.approval_rule_template_name required"
        )
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "DisassociateApprovalRuleTemplateFromRepositoryInput.repository_name required"
        )
    return out
