"""Generated from Smithy shape ``com.amazonaws.codecommit#CreateApprovalRuleTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rule_template


class CreateApprovalRuleTemplateOutput(TypedDict, closed=True):
    approval_rule_template: (
        "aws_sdk_codecommit.types.approval_rule_template.ApprovalRuleTemplate"
    )
    """<p>The content and structure of the created approval rule template.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApprovalRuleTemplateOutput) -> dict:
    out: dict = {}
    import aws_sdk_codecommit.types.approval_rule_template

    out["approvalRuleTemplate"] = (
        aws_sdk_codecommit.types.approval_rule_template.serialize_aws_json_1_1(
            value["approval_rule_template"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApprovalRuleTemplateOutput:
    out: CreateApprovalRuleTemplateOutput = {}  # type: ignore[typeddict-item]
    if "approvalRuleTemplate" in data:
        import aws_sdk_codecommit.types.approval_rule_template

        out["approval_rule_template"] = (
            aws_sdk_codecommit.types.approval_rule_template.deserialize_aws_json_1_1(
                data["approvalRuleTemplate"]
            )
        )
    else:
        raise DeserializationError(
            "CreateApprovalRuleTemplateOutput.approval_rule_template required"
        )
    return out
