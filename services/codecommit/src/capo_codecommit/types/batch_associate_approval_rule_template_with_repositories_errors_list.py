"""Generated from Smithy shape ``com.amazonaws.codecommit#BatchAssociateApprovalRuleTemplateWithRepositoriesErrorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.batch_associate_approval_rule_template_with_repositories_error

BatchAssociateApprovalRuleTemplateWithRepositoriesErrorsList: TypeAlias = list[
    "capo_codecommit.types.batch_associate_approval_rule_template_with_repositories_error.BatchAssociateApprovalRuleTemplateWithRepositoriesError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: BatchAssociateApprovalRuleTemplateWithRepositoriesErrorsList,
) -> list:
    import capo_codecommit.types.batch_associate_approval_rule_template_with_repositories_error

    out: list = []
    for item in value:
        out.append(
            capo_codecommit.types.batch_associate_approval_rule_template_with_repositories_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> BatchAssociateApprovalRuleTemplateWithRepositoriesErrorsList:
    import capo_codecommit.types.batch_associate_approval_rule_template_with_repositories_error

    out: BatchAssociateApprovalRuleTemplateWithRepositoriesErrorsList = []
    for item in data:
        out.append(
            capo_codecommit.types.batch_associate_approval_rule_template_with_repositories_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
