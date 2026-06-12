"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.batch_disassociate_approval_rule_template_from_repositories_error

BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorsList: TypeAlias = list[
    "aws_sdk_codecommit.types.batch_disassociate_approval_rule_template_from_repositories_error.BatchDisassociateApprovalRuleTemplateFromRepositoriesError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorsList,
) -> list:
    import aws_sdk_codecommit.types.batch_disassociate_approval_rule_template_from_repositories_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codecommit.types.batch_disassociate_approval_rule_template_from_repositories_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorsList:
    import aws_sdk_codecommit.types.batch_disassociate_approval_rule_template_from_repositories_error

    out: BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorsList = []
    for item in data:
        out.append(
            aws_sdk_codecommit.types.batch_disassociate_approval_rule_template_from_repositories_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
