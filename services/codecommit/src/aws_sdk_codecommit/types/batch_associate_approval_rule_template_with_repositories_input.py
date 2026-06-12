"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchAssociateApprovalRuleTemplateWithRepositoriesInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.approval_rule_template_name
    import aws_sdk_codecommit.types.repository_name_list


class BatchAssociateApprovalRuleTemplateWithRepositoriesInput(TypedDict):
    approval_rule_template_name: (
        "aws_sdk_codecommit.types.approval_rule_template_name.ApprovalRuleTemplateName"
    )
    """<p>The name of the template you want to associate with one or more repositories.</p>"""
    repository_names: "aws_sdk_codecommit.types.repository_name_list.RepositoryNameList"
    """<p>The names of the repositories you want to associate with the template.</p> <note> <p>The length constraint limit is for each string in the array. The array itself can be empty.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: BatchAssociateApprovalRuleTemplateWithRepositoriesInput,
) -> dict:
    out: dict = {}
    out["approvalRuleTemplateName"] = value["approval_rule_template_name"]
    import aws_sdk_codecommit.types.repository_name_list

    out["repositoryNames"] = (
        aws_sdk_codecommit.types.repository_name_list.serialize_aws_json_1_1(
            value["repository_names"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> BatchAssociateApprovalRuleTemplateWithRepositoriesInput:
    out: BatchAssociateApprovalRuleTemplateWithRepositoriesInput = {}  # type: ignore[typeddict-item]
    if "approvalRuleTemplateName" in data:
        out["approval_rule_template_name"] = data["approvalRuleTemplateName"]
    else:
        raise DeserializationError(
            "BatchAssociateApprovalRuleTemplateWithRepositoriesInput.approval_rule_template_name required"
        )
    if "repositoryNames" in data:
        import aws_sdk_codecommit.types.repository_name_list

        out["repository_names"] = (
            aws_sdk_codecommit.types.repository_name_list.deserialize_aws_json_1_1(
                data["repositoryNames"]
            )
        )
    else:
        raise DeserializationError(
            "BatchAssociateApprovalRuleTemplateWithRepositoriesInput.repository_names required"
        )
    return out
