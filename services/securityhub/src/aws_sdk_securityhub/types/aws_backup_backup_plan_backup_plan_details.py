"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsBackupBackupPlanBackupPlanDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_backup_backup_plan_advanced_backup_settings_list
    import aws_sdk_securityhub.types.aws_backup_backup_plan_rule_list
    import aws_sdk_securityhub.types.non_empty_string


class AwsBackupBackupPlanBackupPlanDetails(TypedDict):
    backup_plan_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The display name of a backup plan. </p>"""
    advanced_backup_settings: NotRequired[
        "aws_sdk_securityhub.types.aws_backup_backup_plan_advanced_backup_settings_list.AwsBackupBackupPlanAdvancedBackupSettingsList"
    ]
    """<p>A list of backup options for each resource type. </p>"""
    backup_plan_rule: NotRequired[
        "aws_sdk_securityhub.types.aws_backup_backup_plan_rule_list.AwsBackupBackupPlanRuleList"
    ]
    """<p>An array of <code>BackupRule</code> objects, each of which specifies a scheduled task that is used to back up a selection of resources. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsBackupBackupPlanBackupPlanDetails) -> dict:
    out: dict = {}
    if "backup_plan_name" in value:
        out["BackupPlanName"] = value["backup_plan_name"]
    if "advanced_backup_settings" in value:
        import aws_sdk_securityhub.types.aws_backup_backup_plan_advanced_backup_settings_list

        out["AdvancedBackupSettings"] = (
            aws_sdk_securityhub.types.aws_backup_backup_plan_advanced_backup_settings_list.serialize_json(
                value["advanced_backup_settings"]
            )
        )
    if "backup_plan_rule" in value:
        import aws_sdk_securityhub.types.aws_backup_backup_plan_rule_list

        out["BackupPlanRule"] = (
            aws_sdk_securityhub.types.aws_backup_backup_plan_rule_list.serialize_json(
                value["backup_plan_rule"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsBackupBackupPlanBackupPlanDetails:
    out: AwsBackupBackupPlanBackupPlanDetails = {}  # type: ignore[typeddict-item]
    if "BackupPlanName" in data:
        out["backup_plan_name"] = data["BackupPlanName"]
    if "AdvancedBackupSettings" in data:
        import aws_sdk_securityhub.types.aws_backup_backup_plan_advanced_backup_settings_list

        out["advanced_backup_settings"] = (
            aws_sdk_securityhub.types.aws_backup_backup_plan_advanced_backup_settings_list.deserialize_json(
                data["AdvancedBackupSettings"]
            )
        )
    if "BackupPlanRule" in data:
        import aws_sdk_securityhub.types.aws_backup_backup_plan_rule_list

        out["backup_plan_rule"] = (
            aws_sdk_securityhub.types.aws_backup_backup_plan_rule_list.deserialize_json(
                data["BackupPlanRule"]
            )
        )
    return out
