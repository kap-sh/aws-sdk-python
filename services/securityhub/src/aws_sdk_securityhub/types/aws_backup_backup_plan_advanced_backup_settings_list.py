"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsBackupBackupPlanAdvancedBackupSettingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_backup_backup_plan_advanced_backup_settings_details

AwsBackupBackupPlanAdvancedBackupSettingsList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_backup_backup_plan_advanced_backup_settings_details.AwsBackupBackupPlanAdvancedBackupSettingsDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsBackupBackupPlanAdvancedBackupSettingsList) -> list:
    import aws_sdk_securityhub.types.aws_backup_backup_plan_advanced_backup_settings_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_backup_backup_plan_advanced_backup_settings_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsBackupBackupPlanAdvancedBackupSettingsList:
    import aws_sdk_securityhub.types.aws_backup_backup_plan_advanced_backup_settings_details

    out: AwsBackupBackupPlanAdvancedBackupSettingsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_backup_backup_plan_advanced_backup_settings_details.deserialize_json(
                item
            )
        )
    return out
