"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsBackupBackupPlanRuleCopyActionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_backup_backup_plan_rule_copy_actions_details

AwsBackupBackupPlanRuleCopyActionsList: TypeAlias = list[
    "capo_securityhub.types.aws_backup_backup_plan_rule_copy_actions_details.AwsBackupBackupPlanRuleCopyActionsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsBackupBackupPlanRuleCopyActionsList) -> list:
    import capo_securityhub.types.aws_backup_backup_plan_rule_copy_actions_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_backup_backup_plan_rule_copy_actions_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsBackupBackupPlanRuleCopyActionsList:
    import capo_securityhub.types.aws_backup_backup_plan_rule_copy_actions_details

    out: AwsBackupBackupPlanRuleCopyActionsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_backup_backup_plan_rule_copy_actions_details.deserialize_json(
                item
            )
        )
    return out
