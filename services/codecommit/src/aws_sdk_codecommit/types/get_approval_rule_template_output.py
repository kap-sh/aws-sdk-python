"""Generated from Smithy shape ``com.amazonaws.codecommit#GetApprovalRuleTemplateOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rule_template


class GetApprovalRuleTemplateOutput(TypedDict):
    approval_rule_template: (
        "aws_sdk_codecommit.types.approval_rule_template.ApprovalRuleTemplate"
    )
    """<p>The content and structure of the approval rule template.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetApprovalRuleTemplateOutput) -> dict:
    out: dict = {}
    import aws_sdk_codecommit.types.approval_rule_template

    out["approvalRuleTemplate"] = (
        aws_sdk_codecommit.types.approval_rule_template.serialize_aws_json_1_1(
            value["approval_rule_template"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetApprovalRuleTemplateOutput:
    out: GetApprovalRuleTemplateOutput = {}  # type: ignore[typeddict-item]
    if "approvalRuleTemplate" in data:
        import aws_sdk_codecommit.types.approval_rule_template

        out["approval_rule_template"] = (
            aws_sdk_codecommit.types.approval_rule_template.deserialize_aws_json_1_1(
                data["approvalRuleTemplate"]
            )
        )
    else:
        raise DeserializationError(
            "GetApprovalRuleTemplateOutput.approval_rule_template required"
        )
    return out
