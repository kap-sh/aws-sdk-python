"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsBackupBackupPlanRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_backup_backup_plan_rule_details

AwsBackupBackupPlanRuleList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_backup_backup_plan_rule_details.AwsBackupBackupPlanRuleDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsBackupBackupPlanRuleList) -> list:
    import aws_sdk_securityhub.types.aws_backup_backup_plan_rule_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_backup_backup_plan_rule_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsBackupBackupPlanRuleList:
    import aws_sdk_securityhub.types.aws_backup_backup_plan_rule_details

    out: AwsBackupBackupPlanRuleList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_backup_backup_plan_rule_details.deserialize_json(
                item
            )
        )
    return out
