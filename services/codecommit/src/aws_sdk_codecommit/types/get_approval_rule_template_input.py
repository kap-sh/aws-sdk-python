"""Generated from Smithy shape ``com.amazonaws.codecommit#GetApprovalRuleTemplateInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rule_template_name


class GetApprovalRuleTemplateInput(TypedDict):
    approval_rule_template_name: (
        "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName"
    )
    """<p>The name of the approval rule template for which you want to get information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetApprovalRuleTemplateInput) -> dict:
    out: dict = {}
    out["approvalRuleTemplateName"] = value["approval_rule_template_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetApprovalRuleTemplateInput:
    out: GetApprovalRuleTemplateInput = {}  # type: ignore[typeddict-item]
    if "approvalRuleTemplateName" in data:
        out["approval_rule_template_name"] = data["approvalRuleTemplateName"]
    else:
        raise DeserializationError(
            "GetApprovalRuleTemplateInput.approval_rule_template_name required"
        )
    return out
