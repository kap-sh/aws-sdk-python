"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsBackupBackupPlanRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_backup_backup_plan_rule_details

AwsBackupBackupPlanRuleList: TypeAlias = list[
    "capo_securityhub.types.aws_backup_backup_plan_rule_details.AwsBackupBackupPlanRuleDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsBackupBackupPlanRuleList) -> list:
    import capo_securityhub.types.aws_backup_backup_plan_rule_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_backup_backup_plan_rule_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsBackupBackupPlanRuleList:
    import capo_securityhub.types.aws_backup_backup_plan_rule_details

    out: AwsBackupBackupPlanRuleList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_backup_backup_plan_rule_details.deserialize_json(
                item
            )
        )
    return out
