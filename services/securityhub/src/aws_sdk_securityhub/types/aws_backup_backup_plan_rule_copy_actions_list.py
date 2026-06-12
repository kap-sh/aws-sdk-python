"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsBackupBackupPlanRuleCopyActionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_backup_backup_plan_rule_copy_actions_details

AwsBackupBackupPlanRuleCopyActionsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_backup_backup_plan_rule_copy_actions_details.AwsBackupBackupPlanRuleCopyActionsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsBackupBackupPlanRuleCopyActionsList) -> list:
    import aws_sdk_securityhub.types.aws_backup_backup_plan_rule_copy_actions_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_backup_backup_plan_rule_copy_actions_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsBackupBackupPlanRuleCopyActionsList:
    import aws_sdk_securityhub.types.aws_backup_backup_plan_rule_copy_actions_details

    out: AwsBackupBackupPlanRuleCopyActionsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_backup_backup_plan_rule_copy_actions_details.deserialize_json(
                item
            )
        )
    return out
