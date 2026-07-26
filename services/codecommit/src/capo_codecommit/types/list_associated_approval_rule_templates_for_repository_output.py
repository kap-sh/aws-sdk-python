"""Generated from Smithy shape ``com.amazonaws.codecommit#ListAssociatedApprovalRuleTemplatesForRepositoryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.approval_rule_template_name_list
    import capo_codecommit.types.next_token


class ListAssociatedApprovalRuleTemplatesForRepositoryOutput(TypedDict, closed=True):
    approval_rule_template_names: NotRequired[
        "capo_codecommit.types.approval_rule_template_name_list.ApprovalRuleTemplateNameList"
    ]
    """<p>The names of all approval rule templates associated with the repository.</p>"""
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that allows the operation to batch the next results of the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListAssociatedApprovalRuleTemplatesForRepositoryOutput,
) -> dict:
    out: dict = {}
    if "approval_rule_template_names" in value:
        import capo_codecommit.types.approval_rule_template_name_list

        out["approvalRuleTemplateNames"] = (
            capo_codecommit.types.approval_rule_template_name_list.serialize_aws_json_1_1(
                value["approval_rule_template_names"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListAssociatedApprovalRuleTemplatesForRepositoryOutput:
    out: ListAssociatedApprovalRuleTemplatesForRepositoryOutput = {}  # type: ignore[typeddict-item]
    if "approvalRuleTemplateNames" in data:
        import capo_codecommit.types.approval_rule_template_name_list

        out["approval_rule_template_names"] = (
            capo_codecommit.types.approval_rule_template_name_list.deserialize_aws_json_1_1(
                data["approvalRuleTemplateNames"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
