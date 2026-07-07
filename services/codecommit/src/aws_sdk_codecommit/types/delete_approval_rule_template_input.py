"""Generated from Smithy shape ``com.amazonaws.codecommit#DeleteApprovalRuleTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rule_template_name


class DeleteApprovalRuleTemplateInput(TypedDict, closed=True):
    approval_rule_template_name: (
        "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName"
    )
    """<p>The name of the approval rule template to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApprovalRuleTemplateInput) -> dict:
    out: dict = {}
    out["approvalRuleTemplateName"] = value["approval_rule_template_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApprovalRuleTemplateInput:
    out: DeleteApprovalRuleTemplateInput = {}  # type: ignore[typeddict-item]
    if "approvalRuleTemplateName" in data:
        out["approval_rule_template_name"] = data["approvalRuleTemplateName"]
    else:
        raise DeserializationError(
            "DeleteApprovalRuleTemplateInput.approval_rule_template_name required"
        )
    return out
