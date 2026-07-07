"""Generated from Smithy shape ``com.amazonaws.codecommit#AssociateApprovalRuleTemplateWithRepositoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rule_template_name
    import aws_sdk_codecommit.types.repository_name


class AssociateApprovalRuleTemplateWithRepositoryInput(TypedDict, closed=True):
    approval_rule_template_name: (
        "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName"
    )
    """<p>The name for the approval rule template. </p>"""
    repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository that you want to associate with the template.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AssociateApprovalRuleTemplateWithRepositoryInput,
) -> dict:
    out: dict = {}
    out["approvalRuleTemplateName"] = value["approval_rule_template_name"]
    out["repositoryName"] = value["repository_name"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> AssociateApprovalRuleTemplateWithRepositoryInput:
    out: AssociateApprovalRuleTemplateWithRepositoryInput = {}  # type: ignore[typeddict-item]
    if "approvalRuleTemplateName" in data:
        out["approval_rule_template_name"] = data["approvalRuleTemplateName"]
    else:
        raise DeserializationError(
            "AssociateApprovalRuleTemplateWithRepositoryInput.approval_rule_template_name required"
        )
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "AssociateApprovalRuleTemplateWithRepositoryInput.repository_name required"
        )
    return out
